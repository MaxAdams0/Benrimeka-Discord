# PS. Annoying but the import name is different from the module
import discord
from discord.ext import commands
import main

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
  await ctx.send(f"`Error: {error}`")
  print(error)

# Bot token, do not publish
client.run("OTA4MjI0MDg2MDE3MjA0MjU0.GjVZc1.1Usx4b5fbrZagYbBOENRqNlaRjeClGxIzXPR28")