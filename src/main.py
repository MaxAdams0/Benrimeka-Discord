# General imports
import discord
from discord.ext import commands
import time
import os

# Variables
path = os.getcwd()

# On start (not discord related)
time_start_raw = round(time.time())
time_start_fiter = time.ctime(time.time())

def time_convert(s):
  s = s % (24 * 86400)
  d = s // 86400
  s %= 86400
  h = s // 3600
  s %= 3600
  m = s // 60
  s %= 60
  return "%02d:%02d:%02d:%02d" % (d, h, m, s)
# Modified ver. of:
# https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/

class main(commands.Cog):
  def __init__(self, client):
    self.client = client

    # Bot imformation commands
    @client.command()
    async def ping(ctx):
      user = str(ctx.author)[0:-5]
      latency = round(client.latency * 1000)
      await ctx.send(f"**Pong!** - {latency}ms")
      print(f"[{user}] CMD: ping")

    # Joke commands
    @client.command()
    async def hit(ctx):
      user = str(ctx.author)[0:-5]
      await ctx.send(file = discord.File(f"{path[:-3]}res\img\hit.jpg"))
      await ctx.send("That's a hit")
      print(f"[{user}] CMD: hit")

    @client.command()
    async def miss(ctx):
      user = str(ctx.author)[0:-5]
      await ctx.send(file = discord.File(f"{path[:-3]}res\img\miss.jpg"))
      await ctx.send("That's a miss")
      print(f"[{user}] CMD: miss")
    
    @client.command()
    async def info(ctx):
      user = str(ctx.author)[0:-5]
      global time_start_raw
      global time_start_fiter
      time_now_raw = round(time.time())

      await ctx.send(f"Bot started on: {time_start_fiter}"+
      f"\nTime since startup: {time_convert(time_now_raw-time_start_raw)}")

      print(f"[{user}] CMD: info")

# Cog setup for current file (main)
def setup(client):
  client.add_cog(main(client))

"""

Features/Changes to add:
- Spotify support

"""