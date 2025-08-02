import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
import random
from config import id_do_servidor, TOKEN

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)
count = 50
# Mensagens para incentivar impulsos/boosts
booster = [
    "<a:Boosts_pinning:1210685364184813598> Seja nossa estrela. Impulsione: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Dê brilho ao servidor: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Nosso céu precisa de você: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Uma constelação te espera. Boost: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Brilhe com a gente: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Seu boost acende estrelas: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Adicione sua luz: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Impulsione e brilhe: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Você é a supernova: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Faça parte do cosmos: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Crie novas galáxias: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Impulsione o firmamento: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Você é a peça celeste: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Seu apoio é estelar: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Suba ao céu com a gente: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Impulsione. Ilumine. <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Junte-se à constelação: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Seja luz, não sombra: <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Brilhar é simples: boost <#1302434570003546142>",
    "<a:Boosts_pinning:1210685364184813598> Toque as estrelas: <#1302434570003546142>"
]

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latência: {round(bot.latency * 1000)}ms")

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
    # Inicia a tarefa de status caso ainda não esteja ativa
    if not status_task.is_running():
        status_task.start()

# Lista de status que combinam com mulheres e garotas
statuses = [
    "💧 BEBA ÁGUA!",
    "🌸 Você é incrível!",
    "👑 Ajuste sua coroa, rainha!",
    "💄 Brilhe hoje!",
    "💖 Ame-se primeiro!",
    "✨ Sorria, linda!",
    "💅 Unhas on point!",
    "🍓 Hora da vitamina!",
    "🎧 Coloque sua música favorita!",
    "📚 Hora do estudo, futura rainha!",
    "☕ Pausa pro café e fofoca!",
    "🧴 Skincare em dia?",
    "👗 Vista-se para si mesma!",
    "🩰 Postura de bailarina!",
    "🧘 Respire fundo, você consegue!",
    "💎 Sua luz é única!",
    "🌈 Espalhe cores hoje!",
    "💌 Envie amor para si mesma!",
    "📸 Capture o momento!",
    "🪞 Olhe no espelho e sorria!"
]

@tasks.loop(minutes=1)
async def status_task():
    """Altera o status do bot periodicamente."""
    await bot.change_presence(activity=discord.Game(name=random.choice(statuses)))

async def load_cogs():
    # Carrega cogs principais
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Cog {filename} carregado com sucesso!")
            except commands.errors.ExtensionAlreadyLoaded:
                print(f"Cog {filename} já estava carregado, ignorando.")
            except Exception as e:
                print(f"Falha ao carregar {filename}: {e}")
                import traceback
                traceback.print_exc()
    
    # Carrega mini-jogos individualmente
    mini_jogos = ["lista", "dado", "coinflip", "rps"]
    for jogo in mini_jogos:
        try:
            await bot.load_extension(f"cogs.mini_jogos.{jogo}")
            print(f"Mini-jogo {jogo} carregado com sucesso!")
        except Exception as e:
            print(f"Falha ao carregar mini-jogo {jogo}: {e}")
            import traceback
            traceback.print_exc()



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
    # Carrega todos os cogs antes de iniciar o bot
    import asyncio
    asyncio.run(load_cogs())
    bot.run(TOKEN)
