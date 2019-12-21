# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:43:00 2019

@author: benja
"""

# SHBot.py

import os

import random

import nest_asyncio
nest_asyncio.apply()

import discord
from discord.ext import commands

from dotenv import load_dotenv

import images as img


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#command prefix
client = commands.Bot(command_prefix='$')


#Randomize list of roles
roles_five_player = ['liberal', 'liberal', 'liberal', 'fascist', 'hitler']
random.shuffle(roles_five_player)
player1 = roles_five_player[0]
player2 = roles_five_player[1]
player3 = roles_five_player[2]
player4 = roles_five_player[3]
player5 = roles_five_player[4]



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
  
 #Receiving a private message confirmation of your ja vote    
@client.command()
async def ja(ctx):
    embed = discord.Embed(title="You have voted Ja!")
    embed.set_image(url=img.imageURL_vote_ja)
    await ctx.author.send(embed = embed)

#Receiving a private message confirmation of your nein vote    
@client.command()
async def nein(ctx):
    embed = discord.Embed(title="You have voted Nein!")
    embed.set_image(url=img.imageURL_vote_nein)
    await ctx.author.send(embed = embed) 

      
        
      

client.run(token)

