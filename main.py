"""
This File is Licensed under MIT
Copyrights © - ImPrabakar 2019-20
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import discord
from discord.ext import commands
import random
from random import randrange
from core import config
import sys
import traceback
import os
import time
import datetime

token = config.token
prefix = config.prefix

bot = commands.Bot(command_prefix=prefix)

initial_extensions = ['cogs.maths',
                      'cogs.admin',
                      'cogs.moderation']

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(f"Failed to load {extension}", file=sys.stderr)
			traceback.print_exc()
			

@bot.event
async def on_ready():
	print("Logged in as")
	print(bot.user.name)
	print(bot.user.id)
	print("Authors: Prabàkár\nNeo-tech-py")
	
@bot.command()
async def ping(ctx):
	"""Shows the latency"""
	await ctx.send(f"Pong! {round(bot.latency * 1000)} ms")
	
@bot.command()
async def dice(ctx):
	"""Rolls a dice"""
	await ctx.send(f"{ctx.message.author.display_name}, You rolled {randrange(1, 7)}")
	
@bot.command(hidden=True)
@commands.is_owner()
async def activity(ctx, game, status=None):
	"""Set the custom status"""
	status = discord.Status[status] if status else discord.Status.online
	game1 = discord.Game(name=game)
	await ctx.bot.change_presence(status=status, activity=game1)
	await ctx.message.delete()
	
@bot.command()
async def members(ctx):
	"""Returns list of members in txt format"""
	server = ctx.guild
	x = server.members
	y = open('members.txt', 'wb')
	for member in x:
		linha = member.name + '\r\n'
		y.write(linha.encode("utf-8"))
	y.close()
	msg = "Members list is ready"
	await ctx.send(msg, file=discord.File('members.txt', 'members.txt'))
	
@bot.command()
async def myinfo(ctx):
	"""Shows the info about author"""
	role = [role for role in ctx.message.author.guild.roles]
	embed = discord.Embed(title=f"Info about - {ctx.message.author.mention}", color=0xccff33, timestap=datetime.datetime.utcfromtimestamp(1553629094))
	embed.set_thumbnail(url=ctx.message.author.avatar_url)
	embed.add_field(name="Id", value=ctx.message.author.id, inline=True)
	embed.add_field(name="Created on", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
	embed.add_field(name=f"Roles ({len(role)})", value=" ".join([role.mention for role in role]), inline=True)
	embed.add_field(name="Top Role", value=ctx.message.author.top_role.mention, inline=True)
	await ctx.send(embed=embed)
	
@bot.command()
async def serverinfo(ctx):
	"""Shows info about the server"""
	roles = [role for role in ctx.guild.roles]
	guild_age = (ctx.message.created_at - ctx.author.guild.created_at).days
	created_at = f"Server created on {ctx.author.guild.created_at.strftime('%b %d %Y at %H:%M')}. That\'s over {guild_age} days ago!"
	online = len({m.id for m in ctx.author.guild.members if m.status is not discord.Status.offline})
	em = discord.Embed(title=f"Guild Info - {ctx.guild.name}", description=created_at, color=discord.Color.blurple())
	em.set_thumbnail(url=ctx.author.guild.icon_url)
	em.set_author(name="Guild Info", icon_url=ctx.author.guild.icon_url)
	em.add_field(name="Name:", value=ctx.author.guild.name)
	em.add_field(name="Id:", value=ctx.author.guild.id)
	em.add_field(name="Online:", value=online)
	em.add_field(name="Total Members:", value=len(ctx.author.guild.members))
	em.add_field(name="Owner:", value=ctx.guild.owner)
	em.add_field(name="Roles:", value=len(roles))
	em.add_field(name="Emojis:", value=len(ctx.guild.emojis))
	em.add_field(name="Region", value=ctx.guild.region)
	em.add_field(name="Verification level", value=ctx.guild.verification_level)
	em.add_field(name="Text Channels:", value=len(ctx.guild.text_channels))
	em.add_field(name="Voice Channels:", value=len(ctx.guild.voice_channels))
	await ctx.send(embed=em)

@bot.command()
async def userinfo(ctx, member: discord.Member):
	"""Shows info about the mentioned member"""
	roles = [role for role in member.roles]
	
	em = discord.Embed(title=f"Userinfo - {member.name}", description=f"Shows Info about {member.name}", color=discord.Color.dark_orange(), timestap=datetime.datetime.utcfromtimestamp(1553629094))
	em.set_thumbnail(url=f"{member.avatar_url}")
	em.add_field(name="ID:", value=member.id)
	em.add_field(name="Guild_Name:", value=member.display_name)
	
	em.add_field(name="Created_at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
	em.add_field(name="Joined_at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
	em.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
	em.add_field(name="Top Role", value=member.top_role.mention)
	em.add_field(name="Bot?", value=member.bot)
	await ctx.send(embed=em)

bot.run(token)
