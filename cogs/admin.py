"""
Copyrights (c) 2019 Prabàkár

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

class Admin(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(hidden=True) # This command will be hidden
	@commands.is_owner()
	async def load(self, ctx, *, cog: str):
		"""Loads a cog (it will work only when the owner of the bot use it). Eg: <prefix>load cogs.<cog>"""
		try:
			self.bot.load_extension(cog)
		except Exception as e:
			print(e) # check your heroku logs
		else:
			await ctx.send(f"**Sucess** - The {cog} has loaded")
			
	@commands.command(hidden=True)
	@commands.is_owner()
	async def unload(self, ctx, *, cog: str):
		"""Unload a cog. This is also a owner only command. Eg: <prefix>unload cogs.<cog>"""
		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			print(e) # check you heroku logs
		else:
			await ctx.send(f"**Sucess** - The {cog} has been unloded")
			
	@commands.command(hidden=True)
	@commands.is_owner()
	async def reload(self, ctx, *, cog: str):
		"""Reloads a cog. This is also a owner only command. Eg: <prefix>reload cogs.<cog>"""
		try:
			self.bot.load_extension(cog)
			self.bot.unload_extension(cog)
		except Exception as e:
			print(e) # check your heroku logs
		else:
			await ctx.send(f"**Sucess** - The {cog} has been reloaded")
			
def setup(bot):
	bot.add_cog(Admin(bot))
