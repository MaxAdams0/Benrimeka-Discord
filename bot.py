import discord
import os
from urllib.request import urlopen

os.system('color')
GREY = '\u001b[38;5;242m'
BLUE = '\u001b[38;5;117m'
GREEN = '\u001b[38;5;115m'
PURPLE = '\u001b[38;5;161m'
ENDC = '\u001b[0m'

bot = discord.Bot()

@bot.event
async def on_ready():
    print('========================================================')
    print(f'{PURPLE}{bot.user}{ENDC} is online!')
    print(f'{GREEN}Ping:{ENDC} {round(bot.latency*1000,1)}ms')
    print('All connected servers:')
    for guild in bot.guilds:
        print(f'{GREY}|  {BLUE}{guild} {GREY}{guild.id}{ENDC}')
    await bot.change_presence(activity=discord.Game('with the API'))
    print('========================================================')

# ======================================================================
# ==================== Voice/Audio Related Commands ====================
# ======================================================================
@bot.slash_command()
async def connect(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.respond(f'Connected to voice channel `{ctx.author.voice.channel}`')
    else:
        await ctx.send('You need to join a voice channel for this command to work')

@bot.slash_command()
async def disconnect(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if (voice.is_connected()):
        await ctx.guild.voice_client.disconnect()
        await ctx.respond(f'Disconnected from voice channel `{ctx.author.voice.channel}`')
    else:
        await ctx.send('I am not currently in a voice channel...')

@bot.slash_command()
async def play(ctx, audio):
    if (audio!='sweden'and
        audio!='interstellar' and
        audio!='badapple' and
        audio!='null' and
        audio!='crabsquid' and
        audio!='lavender'):

        await ctx.respond(f'`{audio}` is not a known audio')
        return
    channel = ctx.author.voice.channel
    if ctx.guild.voice_client:
        voice = ctx.guild.voice_client
    else:
        voice = await channel.connect()
    voice.stop()
    audio_source = discord.FFmpegPCMAudio(source=f'audio/{audio}.mp3', executable='C:/FFmpeg/bin/ffmpeg.exe')
    voice.play(audio_source)
    await ctx.respond(f'Now playing `{audio}`')

@bot.slash_command()
async def pause(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    voice_client.pause()
    if (not voice_client.is_connected()):
        await ctx.respond('Not in voice channel')
    else:
        await ctx.respond('Audio paused')

@bot.slash_command()
async def resume(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if (not voice_client.is_connected()):
        await ctx.respond('Not in voice channel')
    else:
        voice_client.resume()
        await ctx.respond('Audio resumed')

@bot.slash_command()
async def stop(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if (not voice_client.is_connected()):
        await ctx.respond('Not in voice channel')
    else:
        voice_client.stop()
        await ctx.respond('Audio stopped')

# ===============================================================
# ==================== Meme Related Commands ====================
# ===============================================================
@bot.slash_command()
async def amongussy(ctx):
    await ctx.respond('https://c.tenor.com/jUMex_rdqPwAAAAM/among-us-twerk.gif')

# Make sure not to publish the text file
bot.run(open('token.txt').read())

# Plans:
# - Spotify integration
# - Playlist