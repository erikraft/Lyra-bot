import random
import discord
from discord.ext import commands
from discord import app_commands


class Dado(commands.Cog):
    """Comando /roll – roda um dado de 6 faces."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="roll", description="🎲｜Joga um dado de 6 faces")
    async def roll_slash(self, interaction: discord.Interaction):
        resultado = random.randint(1, 6)
        await interaction.response.send_message(f"🎲 Você rolou: **{resultado}**", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Dado(bot))
