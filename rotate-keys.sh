#!/bin/bash
# Rotate API keys without pasting them into a chat window.
# Input is hidden, .env is rewritten, and GitHub secrets are updated to match.
#
#   ./rotate-keys.sh            # rotate all four
#   ./rotate-keys.sh ANTHROPIC_API_KEY GEMINI_API_KEY   # rotate only these
set -euo pipefail
cd "$(dirname "$0")"
REPO="nik-attri/second-brain"
KEYS=("$@")
[ ${#KEYS[@]} -eq 0 ] && KEYS=(ANTHROPIC_API_KEY APIFY_TOKEN TAVILY_API_KEY GEMINI_API_KEY)

declare -A WHERE=(
  [ANTHROPIC_API_KEY]="https://console.anthropic.com/settings/keys"
  [APIFY_TOKEN]="https://console.apify.com/settings/integrations"
  [TAVILY_API_KEY]="https://app.tavily.com/home"
  [GEMINI_API_KEY]="https://aistudio.google.com/apikey"
)

for K in "${KEYS[@]}"; do
  echo ""
  echo "$K  ->  ${WHERE[$K]}"
  printf '  paste new value (hidden, blank to skip): '
  read -rs VAL; echo
  [ -z "$VAL" ] && { echo "  skipped"; continue; }

  touch .env
  grep -v "^${K}=" .env > .env.tmp || true
  printf '%s=%s\n' "$K" "$VAL" >> .env.tmp
  mv .env.tmp .env
  chmod 600 .env
  echo "  .env updated"

  if command -v gh >/dev/null && gh auth status >/dev/null 2>&1; then
    printf '%s' "$VAL" | gh secret set "$K" --repo "$REPO"
    echo "  GitHub secret updated"
  else
    echo "  ! gh not authed - set the secret manually"
  fi
  unset VAL
done

echo ""
echo "Done. Verify with: ./verify-keys.sh"
