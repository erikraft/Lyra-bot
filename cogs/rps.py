import random
import discord
from discord.ext import commands
from discord import app_commands

# Opções do jogo com emoji antes do texto
ESCOLHAS = ["🪨 Pedra", "📄 Papel", "✂️ Tesoura"]

# Mapeia os nomes sem emoji para as versões com emoji
NOMES_EMOJI = {
    "Pedra": "🪨 Pedra",
    "Papel": "📄 Papel",
    "Tesoura": "✂️ Tesoura"
}

def resultado_rps(jogador: str, bot: str) -> str:
    # Gera um resultado aleatório: 0 = empate, 1 = vitória, 2 = derrota
    resultado = random.randint(0, 2)
    
    if resultado == 0:
        return "🤝 Empate!"
    elif resultado == 1:
        return "🎉 Você venceu!"
    else:
        return "😢 Você perdeu!"


class RPS(commands.Cog):
    """Comando /rps – Pedra, Papel ou Tesoura."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="rps", description="🪨｜Jogue Pedra, Papel ou Tesoura contra o bot")
    @app_commands.describe(escolha="Sua escolha: Pedra, Papel ou Tesoura")
    @app_commands.choices(escolha=[
        app_commands.Choice(name="🪨 Pedra", value="🪨 Pedra"),
        app_commands.Choice(name="📄 Papel", value="📄 Papel"),
        app_commands.Choice(name="✂️ Tesoura", value="✂️ Tesoura")
    ])
    async def rps_slash(self, interaction: discord.Interaction, escolha: str):
        # Gera uma escolha aleatória para o bot
        bot_escolha = random.choice(ESCOLHAS)
        
        # Obtém o resultado baseado nas escolhas
        resultado = resultado_rps(escolha, bot_escolha)
        
        # Envia apenas o resultado
        await interaction.response.send_message(resultado)


async def setup(bot: commands.Bot):
    await bot.add_cog(RPS(bot))
