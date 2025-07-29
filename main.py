import discord
from discord.ext import commands
from discord import app_commands
import os
import random
from config import id_do_servidor, TOKEN

intents = discord.Intents.default()
intents.message_content = True  

id_do_servidor = 1391101840682389524 
bot = commands.Bot(command_prefix="!", intents=intents)
count = 30
booster = [
    "Seja nossa estrela. Impulsione: <#1302434570003546142>",
    "Dê brilho ao servidor: <#1302434570003546142>",
    "Nosso céu precisa de você: <#1302434570003546142>",
    "Uma constelação te espera. Boost: <#1302434570003546142>",
    "Brilhe com a gente: <#1302434570003546142>",
    "Seu boost acende estrelas: <#1302434570003546142>",
    "Adicione sua luz: <#1302434570003546142>",
    "Impulsione e brilhe: <#1302434570003546142>",
    "Você é a supernova: <#1302434570003546142>",
    "Faça parte do cosmos: <#1302434570003546142>",
    "Crie novas galáxias: <#1302434570003546142>",
    "Impulsione o firmamento: <#1302434570003546142>",
    "Você é a peça celeste: <#1302434570003546142>",
    "Seu apoio é estelar: <#1302434570003546142>",
    "Suba ao céu com a gente: <#1302434570003546142>",
    "Impulsione. Ilumine. <#1302434570003546142>",
    "Junte-se à constelação: <#1302434570003546142>",
    "Seja luz, não sombra: <#1302434570003546142>",
    "Brilhar é simples: boost <#1302434570003546142>",
    "Toque as estrelas: <#1302434570003546142>"
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
