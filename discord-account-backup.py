import discord
from discord.ext import commands
import requests
from colorama import Fore, init
import ctypes
import os
import datetime
import time
import threading
from pathlib import Path

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)

title("DISCORD BACKUP TOOL BY https://github.com/XINSDEATH")

init(autoreset=True)
white = Fore.RESET
gray = Fore.LIGHTBLACK_EX

os.system("cls")

while True:
    print("input token: ", end="")
    TOKEN = input()
    headers = {'Authorization': f'{TOKEN}'}
    r = requests.get("https://discord.com/api/users/@me", headers=headers)
    if r.status_code == 200:
        print("good job a valid token")
        break
    else:
        headers = {'Authorization': f'Bot {TOKEN}'}
        r = requests.get(f"https://discord.com/api/users/@me", headers=headers)
        if r.status_code == 200:
            print("bro not bot tokens LMFAO")
        else:
            print("invalid token :(")

time.sleep(1)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="399439", self_bot=True, intents=intents)
bot.remove_command("help")

async def main():
    now = datetime.datetime.now()
    folder = f"{os.getcwd()}\\backups\\{now.strftime('%Y-%m-%d %H-%M-%S')}"
    os.makedirs(folder)
    open(folder + "\\friend_users.txt", "x").close()
    open(folder + "\\blocked_users.txt", "x").close()
    open(folder + "\\names.txt", "x").close()
    print("created files and folders")
    
    try:
        f = open(folder + "\\friend_users.txt", "a")
        for friend in bot.user.friends:
            f.write(f"{friend.id} - {friend.name}#{friend.discriminator}\n")
        f.close()
        print("saved friends")
    except:
        print("failed to save friends :(")

    try:
        f = open(folder + "\\blocked_users.txt", "a")
        for blocked in bot.user.blocked:
            f.write(f"{blocked.id} - {blocked.name}#{blocked.discriminator}\n")
        f.close()
        print("saved blocked users")
    except:
        print("failed to save blocked users :(")

    try:
        f = open(folder + "\\names.txt", "a")
        f.write(bot.user.name)
        f.close()
        print("saved names")
    except:
        print("failed to save names :(")
    
    try:
        await bot.user.avatar_url.save(f"{folder}\\pfp.jpg")
        print("saved pfp")
    except:
        print("failed to save pfp :(")
    
    print(f"backup completed")
    print("click the button enter to exit")
    input()
    exit()

os.system("cls")
print("booting up")
async def setup():
    await bot.wait_until_ready()
    await main()
bot.loop.create_task(setup())
bot.run(TOKEN, bot=False)
