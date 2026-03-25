from requests import get
from color import color
from menu import UI
from time import sleep
from inputimeout import TimeoutOccurred, inputimeout
from os import getcwd
import json

ui = UI()

def wait_exit():
    input(f"{color.warning}Press ENTER to exit...{color.reset}")
    raise SystemExit

class data:  
    def __init__(self):
        self.commands = ["hunt", "battle"]
        self.wbm = [30, 120]
        self.OwOID = '408785106942164992'
        self.totalcmd = 0
        self.totaltext = 0
        self.stopped = False
        self.wait_time_daily = 60
        try:
            with open(f'{getcwd()}/settings.json', "r") as file:
                data = json.load(file)
                self.token = data.get("token", "")
                self.channel = data.get("channel", "")
                self.gm = "YES" if data.get("gm") else "NO"
                self.sm = "YES" if data.get("sm") else "NO"
                self.pm = "YES" if data.get("pm") else "NO"
                self.em = {
                    "text": "YES" if data.get("em", {}).get("text") else "NO",
                    "owo": "YES" if data.get("em", {}).get("owo") else "NO"
                }
                self.sbcommands = {
                    "prefix": data.get("sbcommands", {}).get("prefix", "."),
                    "allowedid": data.get("sbcommands", {}).get("allowedid"),
                    "enable": "YES" if data.get("sbcommands", {}).get("enable") else "NO"
                }
                self.webhook = {
                    "link": data.get("webhook", {}).get("link"),
                    "ping": data.get("webhook", {}).get("ping")
                }
                self.daily = "YES" if data.get("daily") else "NO"
                self.stop = data.get("stop", "0")
                self.sell = {
                    "enable": "YES" if data.get("sell", {}).get("enable") else "NO",
                    "types": data.get("sell", {}).get("types", "all")
                }
                self.change = "YES" if data.get("change") else "NO"
                self.dmsID = None
                self.guildID = None
        except FileNotFoundError:
            ui.slowPrinting(f"{color.fail} !!! [ERROR] !!! {color.reset} settings.json not found")
            sleep(2)
            raise SystemExit
        except json.JSONDecodeError:
            ui.slowPrinting(f"{color.fail} !!! [ERROR] !!! {color.reset} Invalid settings.json format")
            sleep(2)
            raise SystemExit

    def check(self):
        if not self.token or not self.channel:
            ui.slowPrinting(f"{color.fail} !!! [ERROR] !!! {color.reset} Please enter Token and Channel ID in settings.json")
            wait_exit()

        else:
            try:
                response = get('https://discord.com/api/v9/users/@me', headers={"Authorization": self.token})
                if not response.ok:
                    ui.slowPrinting(f"{color.fail} !!! [ERROR] !!! {color.reset} Invalid Token")
                    wait_exit()

            except Exception as e:
                ui.slowPrinting(f"{color.fail} !!! [ERROR] !!! {color.reset} Network error: {str(e)}")
                wait_exit()