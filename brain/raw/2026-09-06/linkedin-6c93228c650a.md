---
author: Morad R.
fetched_at: '2026-09-06T07:25:15.509530Z'
id: 6c93228c650a
lane: lead
published: ''
source: linkedin
title: '𝗘𝗺𝗮𝗶𝗹 𝗙𝗼𝗿𝗲𝗻𝘀𝗶𝗰𝘀 (5): 𝗗𝗞𝗜𝗠 (𝗣𝗮𝗿𝘁 2) 🛠️📧


  Now that we know 𝗗𝗞𝗜𝗠 acts as an unbreakable digital wax seal, how do we configu'
url: https://www.linkedin.com/posts/morad-rawashdeh_df-dfir-emailforensics-activity-7502258387351597056-h2pc
---

𝗘𝗺𝗮𝗶𝗹 𝗙𝗼𝗿𝗲𝗻𝘀𝗶𝗰𝘀 (5): 𝗗𝗞𝗜𝗠 (𝗣𝗮𝗿𝘁 2) 🛠️📧

Now that we know 𝗗𝗞𝗜𝗠 acts as an unbreakable digital wax seal, how do we configure it, and how do we investigate it during an incident?

🌍 𝟭. 𝗣𝘂𝗯𝗹𝗶𝘀𝗵𝗶𝗻𝗴 𝘁𝗵𝗲 𝗣𝘂𝗯𝗹𝗶𝗰 𝗞𝗲𝘆
After generating your Private and Public keys on your email gateway (like Cisco Secure Email), you must publish the Public Key so the world can see it. You do this by adding a TXT record to your DNS provider (like Cloudflare).

🔍 𝟮. 𝗧𝗵𝗲 𝗠𝗮𝗴𝗶𝗰 "𝗦𝗲𝗹𝗲𝗰𝘁𝗼𝗿"
A company might have multiple mail servers, which means multiple 𝗗𝗞𝗜𝗠 keys. How does the receiving server know exactly where to look in your DNS for the correct key? It uses a 𝗦𝗲𝗹𝗲𝗰𝘁𝗼𝗿.
When analyzing an email header, look at the `𝗗𝗞𝗜𝗠-𝗦𝗶𝗴𝗻𝗮𝘁𝘂𝗿𝗲:` block to find the `𝘀=` 𝘁𝗮𝗴 (this is the selector).

To investigate a domain's DKIM key manually, use this terminal command format:
`𝙙𝙞𝙜 [𝙨𝙚𝙡𝙚𝙘𝙩𝙤𝙧]._𝙙𝙤𝙢𝙖𝙞𝙣𝙠𝙚𝙮.[𝙙𝙤𝙢𝙖𝙞𝙣.𝙘𝙤𝙢] 𝙏𝙓𝙏`

🛡️ 𝟯. 𝗘𝗻𝗳𝗼𝗿𝗰𝗶𝗻𝗴 𝘁𝗵𝗲 𝗥𝘂𝗹𝗲𝘀
Just like SPF, you can use enterprise security gateways to automate your defense. You can create 𝗖𝗼𝗻𝘁𝗲𝗻𝘁 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 that instantly drop or quarantine emails if the "𝗗𝗞𝗜𝗠 𝗔𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗶𝗼𝗻" results in a `𝗛𝗮𝗿𝗱𝗳𝗮𝗶𝗹` or `𝗣𝗲𝗿𝗺𝗲𝗿𝗿𝗼𝗿`. 

💡 𝗣𝗥𝗢 𝗧𝗜𝗣 𝗳𝗼𝗿 𝗦𝗲𝗻𝗶𝗼𝗿 𝗔𝗻𝗮𝗹𝘆𝘀𝘁𝘀: 𝗧𝗵𝗲 "𝗗𝗞𝗜𝗠 𝗥𝗲𝗽𝗹𝗮𝘆" 𝗔𝘁𝘁𝗮𝗰𝗸 🎭
Did you know that a perfectly valid, mathematically sound DKIM signature can still be used for malicious phishing? It is called a 𝗗𝗞𝗜𝗠 𝗥𝗲𝗽𝗹𝗮𝘆 𝗔𝘁𝘁𝗮𝗰𝗸.

Unlike SPF (which checks the sender's IP address), a DKIM signature travels with the email. An attacker can create a free account on a shared email service (like Microsoft 365 or Google Workspace), send a benign email to an inbox they control, and capture the valid DKIM signature.

They then take that exact, validly signed email and forward it to thousands of your employees using their own servers! Because the original email headers and body haven't changed, the DKIM signature will PASS, completely tricking spam filters into trusting the message.
𝗛𝗼𝘄 𝗱𝗼 𝘄𝗲 𝘀𝘁𝗼𝗽 𝘁𝗵𝗶𝘀? DKIM cannot stop replay attacks on its own. That's why DKIM and SPF must be tied together using 𝗗𝗠𝗔𝗥𝗖 to ensure true security! 🎯

#DF #DFIR #EmailForensics #CyberSecurity #IncidentResponse #BlueTeam #DigitalForensics #InfoSec #ThreatHunting
