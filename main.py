import discord
from discord.ext import commands
from discord import app_commands
import os
import random
from config import TOKEN


intents = discord.Intents.default()
intents.message_content = True  

id_do_servidor = 1391101840682389524 
bot = commands.Bot(command_prefix="!", intents=intents)
count = 30
booster = [
    "<a:Boosts_pinning:1210685364184813598> Hey! Já pensou em impulsionar nosso servidor?",
    "<a:Boosts_pinning:1210685364184813598> Dá aquela força pro server! Impulsiona a gente!",
    "<a:Boosts_pinning:1210685364184813598> Nosso servidor merece brilhar — que tal impulsionar?",
    "<a:Boosts_pinning:1210685364184813598> Você + Boost = servidor lendário. Bora?",
    "<a:Boosts_pinning:1210685364184813598> Tá de bobeira? Impulsiona o server e ganha vantagens!",
    "<a:Boosts_pinning:1210685364184813598> Ajude o servidor a crescer com um boost seu!",
    "<a:Boosts_pinning:1210685364184813598> Chegou a hora de impulsionar quem te diverte.",
    "<a:Boosts_pinning:1210685364184813598> Um boost seu muda tudo. Mostra sua força!",
    "<a:Boosts_pinning:1210685364184813598> O servidor precisa de heróis. Impulsiona lá!",
    "<a:Boosts_pinning:1210685364184813598> Você já impulsionou hoje? Não? Demonstre o seu Boost",
    "<a:Boosts_pinning:1210685364184813598> Impulsionar o servidor não dói e ainda deixa ele lindo.",
    "<a:Boosts_pinning:1210685364184813598> Dá aquele boost maroto pra gente continuar crescendo!",
    "<a:Boosts_pinning:1210685364184813598> Sabe como melhorar tudo por aqui? Com um boost seu.",
    "<a:Boosts_pinning:1210685364184813598> Se você curte aqui, retribui com um impulsinho!",
    "<a:Boosts_pinning:1210685364184813598> Ajude o servidor a subir de nível.",
    "<a:Boosts_pinning:1210685364184813598> Impulsionar é amar. Demonstre o seu Boost",
    "<a:Boosts_pinning:1210685364184813598> Só os verdadeiros impulsionam. Você é um deles?",
    "<a:Boosts_pinning:1210685364184813598> Mostra que você é raiz: impulsiona esse servidor agora!",
    "<a:Boosts_pinning:1210685364184813598> Quer mais vantagens? Impulsiona e descobre",
    "<a:Boosts_pinning:1210685364184813598> É hora de mostrar apoio com estilo. Dá um boost"
]


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latência: {round(bot.latency * 1000)}ms")

@bot.event
async def on_ready():
    print(f"Entramos como {bot.user} (ID: {bot.user.id})")
    print(f"Latência: {round(bot.latency * 1000)}ms")
    try:
        await bot.tree.sync(guild=discord.Object(id_do_servidor))
        print("Comandos slash sincronizados para o servidor.")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
    try:
        await bot.tree.sync()
        print("Comandos slash sincronizados.")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
    print("Bot está pronto!")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Cog {filename} carregado.")
            except Exception as e:
                print(f"Falha ao carregar {filename}: {e}")

@bot.event
async def on_connect():
    await load_cogs()

@bot.event
async def on_message(message):
    global count
    if message.author != bot.user:
        count -= 1
        if count == 0:
            frase = random.choice(booster)
            await message.channel.send(frase)
            count = 50
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)    
