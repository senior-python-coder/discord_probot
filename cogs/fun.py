import random
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dice")
    async def dice(self, ctx, sides: int = 6):
        roll = random.randint(1, sides)
        await ctx.send(f"🎲 You rolled: {roll}")

    @commands.command(name="choose")
    async def choose(self, ctx, *options):
        if not options:
            await ctx.send("❌ Provide options to choose from.")
            return
        choice = random.choice(options)
        await ctx.send(f"🤔 I choose: {choice}")

def setup(bot):
    bot.add_cog(Fun(bot))
