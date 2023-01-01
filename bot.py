import discord
import os
os.system('color')
GREY = '\u001b[30;5;240m'
BLUE = '\u001b[38;5;117m'
GREEN = '\u001b[38;5;115m'
ENDC = '\u001b[0m'

bot = discord.Bot()

@bot.event
async def on_ready():
    print("================================================================================")
    print(f"{BLUE}{bot.user}{ENDC} is online!")
    print(f"{GREEN}Ping:{ENDC} {round(bot.latency*1000,1)}ms")
    print("All connected servers:")
    for guild in bot.guilds:
        print(f"{GREY}|{ENDC} {guild.name} - {guild.id}")
    await bot.change_presence(activity=discord.Game("with the API"))
    print("================================================================================")

# ================================================================
# ==================== Audio Related Commands ====================
# ================================================================
@bot.slash_command(guild_ids=bot.guilds)
async def connect(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.respond(f"Connected to voice channel `{ctx.author.voice.channel}`")
    else:
        await ctx.send("You need to join a voice channel for this command to work")

@bot.slash_command(guild_ids=bot.guilds)
async def disconnect(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if (voice.is_connected()):
        await ctx.guild.voice_client.disconnect()
        await ctx.respond(f"Disconnected from voice channel `{ctx.author.voice.channel}`")
    else:
        await ctx.send("I am not currently in a voice channel...")

@bot.slash_command(guild_ids=bot.guilds)
async def play(ctx, sound=""):
    if (sound!="sweden" or 
        sound!="interstellar" or 
        sound!="badapple"): 

        await ctx.respond(f"`{sound}` is not a known song")
        return
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    audio_source = discord.FFmpegPCMAudio(source=f'music/{sound}.mp3', executable='C:/FFmpeg/bin/ffmpeg.exe')
    voice.play(audio_source)
    await ctx.respond(f"Now playing `{sound}`")

# ===============================================================
# ==================== Meme Related Commands ====================
# ===============================================================
@bot.slash_command(guild_ids=bot.guilds)
async def amongussy(ctx):
    await ctx.send("https://c.tenor.com/jUMex_rdqPwAAAAM/among-us-twerk.gif")

# Make sure not to publish the text file
bot.run(open('token.txt').read())

# Plans:
# - Pause/Resume/Stop
# - Playlist
# - Soundboard