import discord
from discord.ext import commands
from discord import app_commands

class IdCommand(commands.Cog):
    """Comando /listar_comandos para listar comandos disponíveis."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="listar_comandos", description="📄｜Lista os comandos globais no formato </nome_do_comando:id>")
    async def listar_comandos(self, interaction: discord.Interaction):
        # Obtém todos os comandos globais registrados para o bot
        comandos = await interaction.client.tree.fetch_commands()

        # Verifica se há comandos globais registrados
        if comandos:
            # Lista os comandos no formato </nome_do_comando:id>
            lista_comandos = [f'</{comando.name}:{comando.id}>' for comando in comandos]
            resposta = '\n'.join(lista_comandos)
            
            # Envia a resposta como mensagem de resposta à interação
            await interaction.response.send_message(f"**Comandos disponíveis:**\n{resposta}")
        else:
            await interaction.response.send_message("Não há comandos globais registrados.")

async def setup(bot: commands.Bot):
    await bot.add_cog(IdCommand(bot))