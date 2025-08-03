import random
import discord
from discord.ext import commands
from discord import app_commands


class CoinFlip(commands.Cog):
    """Comando /coinflip – cara ou coroa."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="coinflip", description="🪙｜Cara ou coroa")
    async def coinflip_slash(self, interaction: discord.Interaction):
        resultado = random.choice(["Cara", "Coroa"])
        await interaction.response.send_message(f"🪙 Deu **{resultado}**!")


async def setup(bot: commands.Bot):
    await bot.add_cog(CoinFlip(bot))
