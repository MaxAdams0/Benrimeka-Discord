# General imports
import discord
from discord.ui import Button, View
from discord.ext import commands

class spotify(commands.Cog):
  def __init__(self, client):
    self.client = client

    # "Sight" class help from https://www.youtube.com/watch?v=kNUuYEWGOxA
    class Sight(View):
      @discord.ui.button(label="Pause", style=discord.ButtonStyle.green)
      async def toggle_cb(self, button, interaction):
        if button.label == "Pause":
          button.label = "Resume"
        else:
          button.label = "Pause"
        await interaction.response.edit_message(view=self)
      
      @discord.ui.button(label="Loop", style=discord.ButtonStyle.blurple)
      async def loop_cb(self, button, interaction):
        await interaction.response.edit_message(view=self)

      @discord.ui.button(label="KILL", style=discord.ButtonStyle.danger)
      async def kill_cb(self, button, interaction):
        await interaction.response.edit_message(view=self)

    @client.command()
    async def play(ctx, *, search):
      #await ctx.author.voice.channel.connect()
      # button cfallback (functionality)
      view = Sight()
      # send final message
      await ctx.send(f"Now playing: {search}", view=view)

# Cog setup for current file (main)
def setup(client):
  client.add_cog(spotify(client))