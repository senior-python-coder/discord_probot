from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"🏓 Pong! Latency: {latency}ms")

    @commands.command(name="info")
    async def info(self, ctx):
        await ctx.send("ℹ️ Senior-level Discord bot with modular architecture and logging.")

def setup(bot):
    bot.add_cog(Utils(bot))
