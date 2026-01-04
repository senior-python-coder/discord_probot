import logging
from discord.ext import commands
from config import BOT_TOKEN, PREFIX

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("discord_probot")

intents = commands.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

INITIAL_COGS = ["cogs.moderation", "cogs.fun", "cogs.utils"]

@bot.event
async def on_ready():
    logger.info(f"Bot connected as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=commands.Game(name="Senior Discord Bot"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 You don’t have permission for this command.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❓ Unknown command. Try `!help`.")
    else:
        logger.error(f"Error in command {ctx.command}: {error}")
        await ctx.send("⚠️ An unexpected error occurred.")

def main():
    for cog in INITIAL_COGS:
        try:
            bot.load_extension(cog)
            logger.info(f"Loaded extension: {cog}")
        except Exception as e:
            logger.error(f"Failed to load {cog}: {e}")

    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()
