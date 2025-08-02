import discord
from discord.ext import commands
from discord import app_commands


class MiniJogos(commands.Cog):
    """Comando /minijogos para mostrar uma lista de mini jogos disponíveis."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="minijogos", description="🕹️｜Mostra uma lista de mini-jogos disponíveis")
    async def minijogos_slash(self, interaction: discord.Interaction):
        """Envia um embed com mini-jogos que os usuários podem jogar."""
        embed = (
            discord.Embed(
                title="MiniJogos 🎮",
                description="Escolha um mini-jogo abaixo e use o comando correspondente:",
                color=discord.Color.blue(),
            )
            .add_field(name="🎲 Dado", value="`/roll` – Jogue um dado aleatório.", inline=False)
            .add_field(name="🪙 Cara ou Coroa", value="`/coinflip` – Cara ou coroa.", inline=False)
            .add_field(name="⚔️ Pedra-Papel-Tesoura", value="`/rps` – Desafie o bot.", inline=False)
            .add_field(name="💭 Adivinhação", value="`/guess` – Tente adivinhar um número.", inline=False)
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(MiniJogos(bot))
