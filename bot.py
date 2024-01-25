from discord.ext import commands
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_message(ctx):
    print(ctx.content) # Prints empty string

bot.run(token)