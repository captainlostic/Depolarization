# Imports
import time
import asyncio
import threading
import websockets
from ahk import AHK
import robloxpy
import configparser
import nordvpn_switcher

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# Read config file
config = configparser.ConfigParser()
config.read('config.ini')

def updateConfig():
    with open('config.ini', 'w') as f:
        config.write(f)
## if im being fr you dont actually need this but it'll be updated at a later point to actually use the cookies (idk what for)
print("Checking cookie(s)...")

if (config.get('ROBLOX_COOKIES', 'cookie_One')) == '':
    updatedCookie = input("Enter ROBLOX cookie: ")
    config.set('ROBLOX_COOKIES', 'cookie_One', updatedCookie)
    updateConfig()

if robloxpy.Utils.CheckCookie(config.get('ROBLOX_COOKIES', 'cookie_One')) != "Valid Cookie":
    print("ROBLOX cookie_One invalid!")
    exit()

robloxCookie = config.get('ROBLOX_COOKIES', 'cookie_One')

robloxpy.User.Internal.SetCookie(robloxCookie)
# Init prob done idk
instructions = nordvpn_switcher.initialize_VPN(area_input=['United States'])

async def handler(websocket):
    retryLimit = 60
    retry = True
    while True:
        message = await websocket.recv()
        if (message == 'Switch') and retry == True:
            retry = False
            nordvpn_switcher.rotate_VPN(instructions)
            time.sleep(retryLimit)
            retry = True

async def main():
    async with websockets.serve(handler, "localhost", 9999):
        await asyncio.Future()

def Check_Crashes():
    while True:
        ahk = AHK()
        win = ahk.win_get(title='Synapse X - Crash Reporter')
        win.close()
        time.sleep(1)

x = threading.Thread(target=Check_Crashes)
x.start()
asyncio.run(main())