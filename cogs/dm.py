from discord import app_commands
import discord
from discord.ext import commands

class DMCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="dm_user", description="Envia uma mensagem em embed para a DM de um usuário.")
    @app_commands.describe(user="Usuário que receberá a mensagem", mensagem="Conteúdo da mensagem a ser enviada")
    @app_commands.checks.has_permissions(administrator=True)

    async def dm_user(self, interaction: discord.Interaction, user: discord.User, mensagem: str):
        embed = discord.Embed(description=mensagem, color=discord.Color.green())
        embed.set_author(
            name=interaction.guild.name if interaction.guild else "Servidor",
            icon_url=interaction.guild.icon.url if (interaction.guild and interaction.guild.icon) else None
        )

        try:
            await user.send(embed=embed)
            await interaction.response.send_message(f"Mensagem enviada para {user.name}!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("Não consegui enviar a mensagem. O usuário pode estar com DMs fechadas.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Ocorreu um erro: {e}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(DMCog(bot))
