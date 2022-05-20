# General imports
import discord
from discord.ext import commands
# File imports
import main
#import spotify

# Setup/Cogs
client = commands.Bot(command_prefix = "-", case_sensative = False)
cogs = [main]
for i in range(len(cogs)):
  cogs[i].setup(client)

# When bot starts
@client.event
async def on_ready():
  game = discord.Game("with the API")
  await client.change_presence(status=discord.Status.online, activity=game)
  print("Client Ready")

@client.event
async def on_connect():
  print(f"Client Connected - {round(client.latency * 1000)}ms")

@client.event
async def on_command_error(ctx, error):
  # --- Recognised Errors ---
  if "is a required argument that is missing" in str(error):
    await ctx.send("You need to add something more...")

  # --- Other Errors ---
  else:
    await ctx.send(f"`Error: {error}`\nIf you do not understand this message, try -errors")
    print(error)

# Bot token, do not publish
client.run("OTA4MjI0MDg2MDE3MjA0MjU0.YYynmA.3KnkseLG9sU9444NLgD4-v_WV0s")