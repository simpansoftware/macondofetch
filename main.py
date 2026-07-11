import requests
from dotenv import load_dotenv
import os
import sys

load_dotenv()
reset = "\033[0m"
line1 = "    ########                        "
line2 = "   ####    ###                      "
line3 = " ###         ###  #####             "
line4 = "###           ##  ## ### ######     "
line5 = "###    #####  #####   ####  ###     "
line6 = "###   ##  ###  ####   ###   ###     "
line7 = "###   #   ###  ###.  ####   ##      "
line8 = " ###     ###   ###  ## ##  ###      "
line9 = "  ########     ###  #   #  ##       "
line10 = "              ###  ## ## ###        "
line11 = "              ###  ####  ###        "
line12 = "             ####        ##         "
line13 = "             ###         ##.##      "
line14 = "                          ####      "
clearline = "                                    "

lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14]

if os.environ.get("COLORTERM", "").lower() in ("truecolor", "24bit"):
    macondoyellow = "\033[38;2;242;191;64m"
elif "NO_COLOR" in os.environ:
    macondoyellow = ""
    reset = ""
else:
    macondoyellow = "\033[33m"

apikey = os.getenv("APIKEY")
if not apikey:
    thing = input("So it looks like you forgot to set an API key in .env\nEither you set it or you enter it here (write q to exit)\n> ")
    if thing == "q":
        sys.exit()
    else:
        apikey = thing

me_raw = requests.get("https://macondo.hackclub.com/api/auth/me", headers={"Authorization": f"Bearer {apikey}"},)
gold_raw = requests.get("https://macondo.hackclub.com/api/users/balance", headers={"Authorization": f"Bearer {apikey}"},)
streak_raw = requests.get("https://macondo.hackclub.com/api/profile/streaks", headers={"Authorization": f"Bearer {apikey}"},)
streak_json = streak_raw.json()
me_json = me_raw.json()
gold_json = gold_raw.json()
print("")
for i, line in enumerate(lines):
    textthing = macondoyellow + line + reset
    if i == 0:
        print(f"{textthing}{me_json.get("username")}@macondo")
    elif i == 1:
        print(f"{textthing}-----------------------")
    elif i == 2:
        print(f"{textthing}Slack ID: {me_json.get('slack_id')}")
    elif i == 3:
        print(f"{textthing}Balance: {gold_json.get('balance')}")
    elif i == 4:
        print(f"{textthing}Streak: {streak_json.get('current_streak')}")
    elif i == 5:
        print(f"{textthing}Longest streak: {me_json.get('longest_current_streak')}")
    elif i == 6:
        print(f"{textthing}Streak freezes remaining: {me_json.get('streak_freezes_remaining')}")
    else:
        print(textthing)