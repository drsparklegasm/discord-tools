# discord-tools
Scripts for discord automation

# Contents:
1. leaveChannels.py
2. TBD

## LeaveChannels.py

This script will systematically remove one's self from discord PM groups. Optionally you can leave the silently.

Backstory: I had a friend who kept adding me to 3 person chats with them and whomever they wanted to include at the time. It clogged my PM feed so I wrote a quick script to remove them systematically. So yeah fuck you Ehren :D

To use:
1. Open a discord session in any browser
2. Hit F12 to open your browser tools
3. Grab the Authorization token and plug it into the script on line 14
4. In the browser, select the conversation(s) you want to leave and grab each channel ID from the URL.
5. Add each channel ID to the channels list on line 20.

* (if you load the conversation you will have an address of https://discord.com/channels/@me/123456789012345678, where {123456789012345678} is the channel ID.)
