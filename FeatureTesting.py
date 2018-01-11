
 #   filename = "sfsg.txt"
 #   file = open(filename, "r")
 #   count = int(file.readline()) + 1
 #   file.close()
 #   file = open(filename, "w")
 #   file.write(str(count))
 #   await bot.say(custom_emoji_dicr.get(":sofar:", "") + custom_emoji_dicr.get(":sogood:","") + SoFarSoGoodConverter(count))
 #   file.close() 

import random
import time

quoteList = []

def ReadFromFile():
    filename = "quotes.txt"
    file = open(filename, "r")
    for line in file:
        quoteList.append(line)
    file.close()

def AndreSaidThis(quote):
    quote += "\n"
    filename = "quotes.txt"
    file = open(filename, "a")
    file.write(quote)
    file.close()

def AndreOnceSaid():
    for i in range(0, len(quoteList)):
        print("```" + quoteList[i] + "```")

def Ping():
    print ("Sample ping message")

def DeleteTimer(numSeconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while (elapsed < numSeconds):
        elapsed = time.time() - start
        #print(str(elapsed))

Ping()
print("Start")
DeleteTimer(2)
print("End")
Ping()