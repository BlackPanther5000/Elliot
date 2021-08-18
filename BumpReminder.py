import pathlib
import asyncio
import datetime
from attr import validate
import discord

from discord import embeds, message
from globalVariables import client, bumpChannel

bumpTasksEnabled = True

bumpReminderTasks = {
    811369107181666343 : False
}
#Run on bot startup
async def startBumpReminderTask(guild):
    #Get channel
    channel = await client.fetch_channel(bumpChannel[guild.id])
    #Find last "bump success" message
    def bumpMessageCheck(message):
        return (message.author.id == 302050872383242240 and "Bump done :thumbsup:" in message.embeds[0].description)

    def bumpRemindCheck(message):
        return (message.author.id == client.user.id and "Bump the server" in message.embeds[0].description)

    bumpMessage = await getMessage(guild, bumpMessageCheck)

    if bumpMessage == None:
        client.loop.create_task(bumpReminderTask(0, guild))
        return

    #Get time since last bump message
    timeSinceBump = datetime.datetime.utcnow() - bumpMessage.created_at

    #Get time unitl next bump
    timeUntilBump = datetime.timedelta(hours= 2) - timeSinceBump

    bumpRemindMessage = await getMessage(guild, bumpRemindCheck)

    #print(f"bumpRemindMessage.created_at - bumpMessage.created_at ({bumpRemindMessage.created_at} - {bumpMessage.created_at} = {bumpRemindMessage.created_at - bumpMessage.created_at}")

    if bumpRemindMessage != None and (bumpRemindMessage.created_at - bumpMessage.created_at).total_seconds() > 0: 
        bumpReminderTasks[guild.id] = False
        return

    
    
    #Start async task waiting for time until next bump
    client.loop.create_task(bumpReminderTask(timeUntilBump.total_seconds(), guild))


async def getMessage(guild, search):

    #Get channel
    channel = await client.fetch_channel(bumpChannel[guild.id])

    message = await channel.history(limit=50).find(search)
    
    if message == None:
        message = await channel.history(limit=150).find(search)

    if message == None:
        message = await channel.history(limit=1500).find(search)

    if message == None:
        message = await channel.history(limit=None).find(search)

    return message

#Make bump message
def getReminderEmbed(guild):
    embed = discord.Embed(title= "⋅•⋅⊰∙∘☽ Its bump time! ☾∘∙⊱⋅•⋅ <:be:876937712135983203><:ta:876937712022745119>", description= "Bump the server with `!d bump`!", color= 7528669)
    embed.set_thumbnail(url=client.user.avatar_url)
    return embed

#Async tasks
async def bumpReminderTask(waitTime, guild):
    channel = await client.fetch_channel(bumpChannel[guild.id])
    #await channel.send("Time until bump: " + str(waitTime) + "seconds")
    await asyncio.sleep(waitTime)
    await channel.send(embed= getReminderEmbed(guild))
    bumpReminderTasks[guild.id] = False

async def backgroundReminderRestarter(guild):
    if guild.id not in bumpReminderTasks.keys(): return
    if guild.id not in bumpChannel.keys(): return
    print(f"Bump reminder task starter started for guild {guild.name}")
    while bumpTasksEnabled == True:
        if not bumpReminderTasks[guild.id]:
            await startBumpReminderTask(guild)
            bumpReminderTasks[guild.id] = True
        await asyncio.sleep(600)
