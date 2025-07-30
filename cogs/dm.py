from discord import app_commands, Interaction, Member, Embed, User
import discord
from discord.ext import commands
from typing import Optional

class DMCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="dm_user", description="Envia uma mensagem em embed para a DM de um usuário.")
    @app_commands.describe(user="Usuário que receberá a mensagem", mensagem="Conteúdo da mensagem a ser enviada")
    @app_commands.checks.has_permissions(administrator=True)
    async def dm_user(self, interaction: Interaction, user: User, *, mensagem: str) -> None:
        embed = Embed(description=mensagem, color=discord.Color.black())
        
        if interaction.guild:
            embed.set_author(
                name=interaction.guild.name,
                icon_url=interaction.guild.icon.url if interaction.guild.icon else None
            )
        else:
            embed.set_author(name="Mensagem do Servidor")

        try:
            await user.send(embed=embed)
            await interaction.response.send_message(f"Mensagem enviada para {user.name}!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message(
                "Não consegui enviar a mensagem. O usuário pode estar com DMs fechadas.", 
                ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(f"Ocorreu um erro: {e}", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DMCog(bot))
