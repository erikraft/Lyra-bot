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
    if jogador == bot:
        return "🤝 Empate!"
        
    ganha = {
        "🪨 Pedra": "✂️ Tesoura",
        "✂️ Tesoura": "📄 Papel",
        "📄 Papel": "🪨 Pedra"
    }
    
    if ganha[jogador] == bot:
        return "🎉 Você venceu!"
    return "😢 Você perdeu!"


class RPS(commands.Cog):
    """Comando /rps – Pedra, Papel ou Tesoura."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="rps", description="✂️｜Jogue Pedra, Papel ou Tesoura contra o bot")
    @app_commands.describe(escolha="Sua escolha: Pedra, Papel ou Tesoura")
    @app_commands.choices(escolha=[
        app_commands.Choice(name="🪨 Pedra", value="🪨 Pedra"),
        app_commands.Choice(name="📄 Papel", value="📄 Papel"),
        app_commands.Choice(name="✂️ Tesoura", value="✂️ Tesoura")
    ])
    async def rps_slash(self, interaction: discord.Interaction, escolha: str):
        bot_escolha = random.choice(ESCOLHAS)
        resultado = resultado_rps(escolha, bot_escolha)
        await interaction.response.send_message(
            f"Você escolheu **{escolha}**. O bot escolheu **{bot_escolha}**. {resultado}"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(RPS(bot))
