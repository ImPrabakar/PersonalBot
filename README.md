<div align="center">
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors)
<img src="https://i.ibb.co/Fbp9GJ9/Pics-Art-09-26-03-44-18.jpg">
</div>
<hr>

# About
**PersonalBot** - It is an open source application. This is bot is recommended for personal use. It can do moderation and other functions. This bot is a simple bot and contains various utilities. This bot is very usefull for guild owners, mods to ease their work. Thia bot is still under development, updated will occupies more commands. Current version is 0.0.1

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
After Adding your cog go to `main.py` in initial_extension mention your filename in which the code exist, mention the cig name as the filename execpt .py. Wait for few minutes, your cog will be added.

# Contributing
Feel free to contribute, an extra hand to support is always welcomed. 

* Find error or add good Commands
* Create a branch 
* Commit
* Open a pull request

# License
This preoject is licensed under MIT

Copyrights (c) Prabàkár 2019

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://imprabakar.github.io/"><img src="https://avatars3.githubusercontent.com/u/55774504?v=4" width="100px;" alt="Prabàkár"/><br /><sub><b>Prabàkár</b></sub></a><br /><a href="#design-ImPrabakar" title="Design">🎨</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!