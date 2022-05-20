# General imports
import discord
from discord.ext import commands
import time

# Variables
directory = "E:\Coding\Servers\Discord"

# On start (not discord related)
time_start_raw = round(time.time())
time_start_fiter = time.ctime(time.time())

def time_convert(seconds):
  seconds = seconds % (24 * 86400)
  days = seconds // 86400
  seconds %= 86400
  hours = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60
  return "%02d:%02d:%02d:%02d" % (days, hours, minutes, seconds)
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
      await ctx.send(file = discord.File(f"{directory}\img\hit.jpg"))
      await ctx.send("That's a hit")
      print(f"[{user}] CMD: hit")

    @client.command()
    async def miss(ctx):
      user = str(ctx.author)[0:-5]
      await ctx.send(file = discord.File(f"{directory}\img\miss.jpg"))
      await ctx.send("That's a miss")
      print(f"[{user}] CMD: miss")
    
    # Suggestions for me to add for the bot
    @client.command()
    async def suggest(ctx, *, message):
      user = str(ctx.author)[0:-5]
      # Suggest - Read
      if message.lower()=="read":
        with open(f"{directory}\\txt\ideas.txt","r") as f:
          content = f.read()
          if len(content)>0 and len(content)<2000:
            await ctx.send(f"{content}\n{len(content)} characters, 1 page")
            print(f"[{user}] CMD: suggest: read")
          elif len(content)>2000:
            for i in range(round(len(content)/2000+0.5)):
              await ctx.send(f"{content[i*2000:(i+1)*2000]}")
              print(f"[{user}] CMD: suggest: read - page {i+1}/{round(len(content)/2000+0.5)}")
            await ctx.send(f"{len(content)} characters, {i+1} pages")
          else:
            await ctx.send("(This file seems to be empty...)")
            print(f"[{user}] CMD: suggest: read - file is empty")
          f.close()
      # Suggest - Remove
      elif message.lower()=="clear":
        with open(directory+"\\txt\ideas.txt","w") as f:
          f.close()
        await ctx.send(f"[{user}] cleared all suggestions")
        print(f"[{user}] CMD: suggest: clear")
      # Suggest - Write
      else:
        with open(directory+"\\txt\ideas.txt","a+") as f:
          f.write(f"{message} - {user}\n")
          f.close()
        print(f"[{user}] CMD: suggest: write - '{message}'")
    
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
Features/Changes being worked on:

Medium
- Buttons

---------------------------------------------------------------

Features/Changes to add:

Large
- Spotify support

Medium
- Help command for list of commands and possible known errors

Small
- Fix directory and anything else that makes this bot not modular
- Add server name and channel to debug print statements (var so can be used elsewhere)

IDK
- Last update?
- Patch/Feature release messages?
- Show message count of all users
- Mass delete messages
"""