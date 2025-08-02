import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
    """Comando /ping para checar latência."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="🏓｜Mostra a latência do bot")
    async def ping_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"🏓 Pong! Latência: {round(self.bot.latency * 1000)}ms",
            ephemeral=True
        )

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
