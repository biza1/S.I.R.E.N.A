
#TODO LIST:
#           DONE) Rehacer lista de frases
#           DONE) Conquista del bot en catacumbas (cambiarle el nombre? Nuevo canal?)
#           DONE) regañar si alguien insulta
#          DONE) Meterse en el canal de voz       
#           DONE) Que salude el bot
#           6) Grabar conversaciones???? [HARD]
#           7) Emitir sonidos
#           DONE) comando ?dinero
#           DONE) comando ?movildedani
#           10) 0:50


import discord
import nest_asyncio
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient
import random
from bd2 import *
import io
import os, os.path



nest_asyncio.apply()



def checkNumberFile(dir):
    list = os.listdir(dir)
    number_files = len(list)
    return number_files 


def randomImage(i):
    return random.randint(1,i)



class Voz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        
        await channel.connect()

    @commands.command()
    async def end(self,ctx):
        await ctx.voice_client.disconnect()

        
        
bot = commands.Bot(command_prefix= commands.when_mentioned_or("?"), description="UH?")    
    
@bot.event
async def on_ready():
    print('Logeado cliente: ')
    print('SOY: {0} ({0.id})'.format(bot.user))
    print('------')
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    texto = MD_TEXTO
    
    if message.author == bot.user:
        return

    if ("sirena" or "sirenita") in message.content.lower():
        r1 = random.randint(0,len(texto)-1)
        await message.reply(texto[r1], mention_author=True)
        return
        
    for e in PALABRAS_BANEADAS:
        if e in message.content.lower():
            r2 = random.randint(0,len(REGAÑAR)-1)
            await message.reply(REGAÑAR[r2], mention_author=True)
            return
        
    for d in DETECTOR_DIOS:
        if d in message.content.lower():
            r3 = random.randint(0, len(REZO)-1)
            emoji = "\U0001F64F"
            await message.add_reaction(emoji)
            await message.reply(REZO[r3], mention_author=True)
            return
        
    if message.content.lower() in SALUDOS:
        r4 = random.randint(0,len(SALUDOS)-1)
        await message.reply(SALUDOS[r4], mention_author=True)
        return
    
    if "pute" in message.content.lower():
        await message.reply("Te felicito por el lenguaje inclusivo, máquina.", mention_author=True)
        return
    
    
#@bot.event
#async def locura():
#    await bot.wait_until_ready()
#    canal =bot.get_channel(375982907019231233)
#    while True == True:
#        print("ole")
#        if True == True:
#            message = random.choice(ELDENRING)
#            await canal.send(message)
#            time = 43
#        await asyncio.sleep(time)
        

@bot.command(pass_context=True)
async def robot(ctx):
    path = r"C:\Users\warbo\Desktop\Cosas\proyecto\BOT DISCORD\robot"
    n = checkNumberFile(path)
    r1 = randomImage(n)
    channel = bot.get_channel(845801368258347028)
    await channel.send(file=discord.File(path+ "\\" + str(r1) + ".png"))


@bot.command(pass_context=True)
async def esqueleto(ctx):
    path = r"C:\Users\warbo\Desktop\Cosas\proyecto\BOT DISCORD\esqueletos"
    n = checkNumberFile(path)
    r1 = randomImage(n)
    channel = bot.get_channel(717759731833503854)
    await channel.send(file=discord.File(path+ "\\" + str(r1) + ".png"))       
    
@bot.command(pass_context=True)
async def elige(ctx, *choices: str):
    await ctx.send(random.choice(choices))
    
@bot.command(pass_context=True)
async def dinero(ctx):
    await ctx.author.send("https://www.paypal.com/servelgar")
    
@bot.command(pass_context=True)   
async def movildedani(ctx):
    g = "https://www.google.com/maps/@"
    r1 = random.randint(0, len(GOOGLE_MAPS)-1)
    latitud = float(random.randint(-200.0000, 200.0000))
    longitud = float(random.randint(-200.0000,200.0000))
    g += str(latitud)
    g += ","
    g += str(longitud)
    g += ",10z"
    embed = discord.Embed(title = "AQUÍ ESTA", url = g, description=GOOGLE_MAPS[r1],color=0xFF5733)
    await ctx.send(embed=embed)
    
@bot.command(pass_context=True)
async def saythankyou(ctx):
    await ctx.author.send("https://www.youtube.com/watch?v=USUdSeeOB1c")

@bot.command(pass_context=True)
async def eldenring(ctx):
    path = r"C:\Users\warbo\Desktop\Cosas\proyecto\BOT DISCORD\audio"
    n = checkNumberFile(path) - 1
    r1 = randomImage(n)
    print("NUMERO ALEATORIO VOZ --> "+str(r1))
    query = path + "\\" + str(r1) + ".mp3"
    author = ctx.message.author 
    canal_voz = author.voice.channel
    print("UNIDO A ---------> "+str(canal_voz))
    canal = None
    if canal_voz != None:
        canal = canal_voz.name 
        vc = await canal_voz.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source = query))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1000.0
        while vc.is_playing():
        
            await asyncio.sleep(5)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name)+ " NO ESTÁ")
    
    await ctx.message.delete()
    
    
@bot.command(pass_context=True)
async def eldenringMAXIMO(ctx):
    path= r"C:\Users\warbo\Desktop\Cosas\proyecto\BOT DISCORD\audio\audio2"
    query = path + "\\" + "destruccion.mp3"
    author = ctx.message.author 
    canal_voz = author.voice.channel 
    print("UNIDO A ----------> "+str(canal_voz))
    canal = None
    if canal_voz != None:
        canal = canal_voz.name 
        vc = await canal_voz.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source = query))
        while vc.is_playing():
            await asyncio.sleep(5)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name)+" NO ESTA EN EL CANAL DE VOZ")
        
    await ctx.message.delete()


    
PERMISION_INTEGER = 473430336

bot.add_cog(Voz(bot))
#bot.loop.create_task(locura())
bot.run("ODQ1NjI2OTI0MDc1MDU3MTky.YKjtcQ.0mqcIzc2mzWhy14c2XuxrNmaXkY")

