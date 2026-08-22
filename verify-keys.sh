#!/bin/bash
# Confirm every key in .env actually works. Prints status only, never values.
cd "$(dirname "$0")"
set -a; . ./.env; set +a
PY=./.venv/bin/python

echo "ANTHROPIC : $($PY -c "
import anthropic,sys
try:
    anthropic.Anthropic().messages.create(model='claude-opus-5',max_tokens=4,
        messages=[{'role':'user','content':'hi'}]); print('OK')
except Exception as e: print('FAIL', type(e).__name__)
" 2>/dev/null)"

echo "APIFY     : $(curl -s -o /dev/null -w '%{http_code}' \
  "https://api.apify.com/v2/users/me?token=$APIFY_TOKEN" | grep -q 200 && echo OK || echo FAIL)"

echo "TAVILY    : $(curl -s -o /dev/null -w '%{http_code}' -X POST https://api.tavily.com/search \
  -H "Authorization: Bearer $TAVILY_API_KEY" -H 'Content-Type: application/json' \
  -d '{"query":"test","max_results":1}' | grep -q 200 && echo OK || echo FAIL)"

echo "GEMINI    : $(curl -s -o /dev/null -w '%{http_code}' \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" -H 'Content-Type: application/json' \
  -d '{"contents":[{"role":"user","parts":[{"text":"hi"}]}]}' | grep -q 200 && echo OK || echo FAIL)"
