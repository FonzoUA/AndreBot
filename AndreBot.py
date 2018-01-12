""" Discord Bot by FonzoUA """
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import time

bot = commands.Bot(description="AndreBot by FonzoUA", command_prefix = '!', p_help = True)

quoteList = []

custom_emoji_dicr = {
    ":test:" : "Test message",
    ":sofar:" : "<:sofar:363110931485425674>",
    ":sogood:" : "<:sogood:363110931523174415>",
    ":sfsg0:" : "<:sfsg0:363110930562678785>",
    ":sfsg1:" : "<:sfsg1:363110931045154817>",
    ":sfsg2:" : "<:sfsg2:363110931162726402>",
    ":sfsg3:" : "<:sfsg3:363110930885902349>",
    ":sfsg4:" : "<:sfsg4:363110930969788417>",
    ":sfsg5:" : "<:sfsg5:363110930868994051>",
    ":sfsg6:" : "<:sfsg6:363110931435225088>",
    ":sfsg7:" : "<:sfsg7:363110931410059264>",
    ":sfsg8:" : "<:sfsg8:363110931439419392>",
    ":sfsg9:" : "<:sfsg9:363110931091161090> ",
    ":thonk:" : "<:thonk:319987819533828097>",
    ":andreears:" : "<:andrenears:360505226156834826>"
}

@bot.event
async def on_ready():
    print("-----------")
    print("Starting bot")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + bot.user.id)
    print("-----------")


@bot.command()
async def Debug():
    message = await bot.say("<Access Error>" + custom_emoji_dicr.get(":andrenears:", ""))
    DeleteTimer(3)
    await bot.delete_message(message)

@bot.command()
async def ping():
    n = random.randint(0,2)
    if n > 0:
        message = await bot.say("So far so good" + custom_emoji_dicr.get(":andreears:",""))
        DeleteTimer(4)
        await bot.delete_message(message)
    elif n == 0:
        message = await bot.say("Go raw and get the job done" + custom_emoji_dicr.get(":andreears:",""))
        DeleteTimer(4)
        await bot.delete_message(message)

@bot.command()
async def sfsg():
    filename = "sfsg.txt"
    file = open(filename, "r")
    count = int(file.readline()) + 1
    file.close()
    file = open(filename, "w")
    file.write(str(count))
    message = await bot.say(custom_emoji_dicr.get(":sofar:", "") + custom_emoji_dicr.get(":sogood:","") + SoFarSoGoodConverter(count))
    DeleteTimer(4)
    await bot.delete_message(message)
    file.close() 

@bot.command()
async def HowIsItSoFar():
    filename = "sfsg.txt"
    file = open(filename, "r")
    count = int(file.readline())
    await bot.say("There have been " + SoFarSoGoodConverter(count) + " " + custom_emoji_dicr.get(":sofar:", "") + custom_emoji_dicr.get(":sogood:","") + "s")
    file.close()

@bot.command()
async def NotSoGoodAnymore(): 
    filename = "sfsg.txt"
    file = open(filename, "w")
    file.write(str(0))
    message = await bot.say(custom_emoji_dicr.get(":thonk:", ""))
    DeleteTimer(4)
    await bot.delete_message(message)
    file.close() 

@bot.command()
async def AndreSaid(quote):
    if (quote == None):
         await bot.say("What did I say " + custom_emoji_dicr.get(":thonk:", "") + " ==> !AndreSaid <text> ")
    quote += "\n"
    filename = "quotes.txt"
    file = open(filename, "a")
    file.write(" > " + quote)
    file.close()
    message = await bot.say("Andre will remember that")
    DeleteTimer(4)
    await bot.delete_message(message)

@bot.command()
async def AndreOnceSaid():
    botstring = "```"

    filename = "quotes.txt"
    file = open(filename, "r")
    for line in file:
        botstring += line
    file.close()
    
    botstring += "```"
    await bot.say(botstring)

def SoFarSoGoodConverter(number):
    result = ""
    for n in str(number):
        result += (custom_emoji_dicr.get(":sfsg" + str(n)+":"))
    return result

def DeleteTimer(numSeconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while (elapsed < numSeconds):
        elapsed = time.time() - start

bot.run("BOT KEY")
