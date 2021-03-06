import discord
from discord.ext import commands
import launcher

class core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.bot.load_extension("extensions." + extension)
        await ctx.send(f"Loaded Extension: {extension}.py")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.bot.unload_extension("extensions." + extension)
        await ctx.send(f"Unloaded Extension: {extension}.py")

    @commands.command(name="reload")
    @commands.has_permissions(administrator=True)
    async def reload_(self, ctx, extension):
        if extension == "all":
            for e in bot.EXTENSIONS:
                self.bot.reload_extension(e)
            await ctx.send(f"Reloaded All Extension.")
        else:
            self.bot.reload_extension("extensions." + extension)
            await ctx.send(f"Reloaded Extension: {extension}.py")

def setup(bot):
    bot.add_cog(core(bot))