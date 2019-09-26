<div align="center">
<img src="https://i.ibb.co/Fbp9GJ9/Pics-Art-09-26-03-44-18.jpg">
</div>
<hr>

# About
**PersonalBot** - It is an open source application. This is bot is recommended for personal use. It can do moderation and other functions. This bot is a simple bot and contains various utilities. This bot is very usefull for guild owners, mods to ease their work

This bot is free for all and it will be always free. If you like this project and want to encourge it donate [@Patreon](https://patreon.com/PrabaRock7) => cool features are there check it out now!

# Getting Started

## Perquisites 
* A [Heroku](https://heroku.com) account
* Fork of this Repo
* A discord bot (You can get from [`here`](https://discordapp.com/developers))
* Calmness 

## Installation 
After cteating a heroku account, Copy your bot token and prefix must be a good prefix.

<a href="https://heroku.com/deploy?template=https://github.com/ImPrabakar/PersonalBot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a><br>
Click this button, it will redirect you to a webpage, there you have to input your name and in config vars, `token` represents your bot token and `prefix` represents your bot prefix. After filling all click deploy button and after it starts to build your app. After completion click manage app button, you will redirect to dashboard and go to resource tab and on that dyno, after few minutes your bot will come online, if not see the logs.

## Adding your own Cog
If you want to make your own cog, make code, upload on the `cogs` folder.

**Example Of cog**

```python3
import discord
from discord.ext import commands

class MyCog(commands.Cog):
  
   def __init__(self, bot):
     self.bot = bot
     
   @commands.command()
   async def hi(self, ctx): # Self must be the first argument 
     await ctx.send(f"hi {ctx.message.author.mention}")
     
def setup(bot): # setup function is important 
  bot.add_cog(MyCog(bot))
```
After Adding your cog go to `main.py` in initial_extension add your cog as "cogs.<cogfilename>" & , (comma) if you add more that one cog,
  
## Finalising and Updating
p
