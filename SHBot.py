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
from dotenv import load_dotenv

import images as img

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

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
    
@client.event
async def on_message(message):
    #Making sure bot doesn't respond to itself
    if message.author == client.user:
        return
    #Embed with text + image for ja and nein votes
    #Need to still have this sent back & forth between messages
    if message.content.startswith('$ja'):
        embed = discord.Embed(title="You have voted Ja!")
        embed.set_image(url=img.imageURL_vote_ja)
        await message.channel.send(embed = embed)
        
    if message.content.startswith('$nein'):
        embed = discord.Embed(title="You have voted Nein!")
        embed.set_image(url=img.imageURL_vote_nein)
        await message.channel.send(embed = embed)
       
    if message.content.startswith('$role'):
        embed = discord.Embed(title="Your role for this game is:")
        embed.set_image(url=random.choice([img.imageURL_role_hitler,img.imageURL_role_fascist,img.imageURL_role_liberal]))
        await message.channel.send(embed = embed)
        
      

client.run(token)

