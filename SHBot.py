# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:13:41 2019

@author: benja
"""

# SHBot.py

import os

import nest_asyncio
nest_asyncio.apply()

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)

