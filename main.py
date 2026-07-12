import requests
from dotenv import load_dotenv
import os
import sys
import shutil

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

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m" 
magenta = "\033[35m"
cyan = "\033[36m"

lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14]

ttywidth = shutil.get_terminal_size().columns

if os.environ.get("COLORTERM", "").lower() in ("truecolor", "24bit"):
    macondoyellow = "\033[38;2;242;191;64m"
elif "NO_COLOR" in os.environ:
    macondoyellow = ""
    red = ""
    cyan = ""
    green = ""
    blue = ""
    magenta = ""
    yellow = ""
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


session = requests.Session()

session.headers.update({"Authorization": f"Bearer {apikey}"})
print("Fetching data from Macondo API...", end="", flush=True)
try:
    me_raw = session.get("https://macondo.hackclub.com/api/auth/me", timeout=10)
    gold_raw = session.get("https://macondo.hackclub.com/api/users/balance", timeout=10)
    starfruit_raw = session.get("https://macondo.hackclub.com/api/users/starfruit", timeout=10)
    streak_raw = session.get("https://macondo.hackclub.com/api/profile/streaks", timeout=10)
    shop_raw = session.get("https://macondo.hackclub.com/api/shop/items", timeout=10)
    shop_json = shop_raw.json()
    starfruit_json = starfruit_raw.json()
    streak_json = streak_raw.json()
    me_json = me_raw.json()
    gold_json = gold_raw.json()
    print("\r" + " " * ttywidth + "\r", end="", flush=True)
except Exception as e:
    print(f"\n{red}thy api requests failed, enter an api key and make sure you are connected to the internet{reset}")
    print(f"{red}Error: {e}{reset}")
    sys.exit()
for i, line in enumerate(lines):
    textthing = macondoyellow + line + reset
    if i == 0:
        print(f"{textthing}{macondoyellow}{me_json.get("username")}@macondo{reset}")
    elif i == 1:
        print(f"{textthing}----------------------------")
    elif i == 2:
        print(f"{textthing}{macondoyellow}Slack ID:{reset} {me_json.get('slack_id')}")
    elif i == 3:
        print(f"{textthing}{macondoyellow}Balance:{reset} {gold_json.get('balance')}")
    elif i == 4:
        print(f"{textthing}{macondoyellow}Starfruit in balance:{reset} {starfruit_json.get('balance')}")
    elif i == 5:
        print(f"{textthing}{macondoyellow}Starfruit earnt in your lifetime:{reset} {starfruit_json.get('lifetime_earned')}")
    elif i == 6:
        print(f"{textthing}{macondoyellow}Shop items:{reset} {len(shop_json.get('items'))}")
    elif i == 7:
        print(f"{textthing}{macondoyellow}Streak:{reset} {streak_json.get('current_streak')}")
    elif i == 8:
        print(f"{textthing}{macondoyellow}Longest streak:{reset} {me_json.get('longest_current_streak')}")
    elif i == 9:
        print(f"{textthing}{macondoyellow}Streak freezes remaining:{reset} {me_json.get('streak_freezes_remaining')}")
    elif i == 10:
        if streak_json.get('today_seconds_logged') >= streak_json.get('daily_goal_seconds'):
            thingamajig = f"{textthing}{macondoyellow}You have worked 100% of your daily goal{reset} (Goal is {round(streak_json.get('daily_goal_seconds') / 3600)} hour" # welcome to cursed hacks 101 where we do cursed hacks
            if round(streak_json.get('daily_goal_seconds') / 3600) == 1:
                print(f"{thingamajig})")
            else:
                print(f"{thingamajig}s)")
        else:
            percentage = round(streak_json.get('today_seconds_logged') / streak_json.get('daily_goal_seconds') * 100)
            initminute = round(streak_json.get('today_seconds_logged') / 60)
            goal = round(streak_json.get('daily_goal_seconds') / 60)
            print(f"{textthing}{macondoyellow}You have worked {percentage}% of your daily goal{reset} ({initminute} minutes out of {goal} minutes)")
    elif i == 11:
        print(f"{textthing}{macondoyellow}Projects: {reset}{len(streak_json.get('projects'))}")        
    elif i == 13:
        print(f"{textthing}{macondoyellow}██{red}██{green}██{yellow}██{blue}██{magenta}██{cyan}██{reset}")
    else:
        print(textthing)