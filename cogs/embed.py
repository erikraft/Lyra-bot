import discord
from discord import app_commands, Interaction
from discord.ext import commands
from datetime import datetime
from typing import Optional

class EmbedBuilderView(discord.ui.View):
    def __init__(self, bot: commands.Bot, interaction: Interaction):
        super().__init__(timeout=300)
        self.bot = bot
        self.interaction = interaction

        self.embed = discord.Embed(color=discord.Color.blue())
        self.embed.description = "Use os botões abaixo para editar o embed."

        self.message = None

    async def start(self):
        self.message = await self.interaction.response.send_message(
            embed=self.embed,
            view=self,
            ephemeral=True
        )

    class EditTituloModal(discord.ui.Modal, title="Editar título do embed"):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            self.titulo = discord.ui.TextInput(label="Título", max_length=256, required=False)
            self.add_item(self.titulo)

        async def on_submit(self, interaction: discord.Interaction):
            novo_titulo = self.titulo.value.strip()
            self.parent.embed.title = novo_titulo if novo_titulo else None
            await self.parent.update_message(interaction)

    class EditDescricaoModal(discord.ui.Modal, title="Editar descrição do embed"):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            self.descricao = discord.ui.TextInput(label="Descrição", style=discord.TextStyle.paragraph, max_length=4000)
            self.add_item(self.descricao)

        async def on_submit(self, interaction: discord.Interaction):
            self.parent.embed.description = self.descricao.value
            await self.parent.update_message(interaction)

    class EditImagemModal(discord.ui.Modal, title="Editar URL da imagem grande"):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            self.url = discord.ui.TextInput(label="URL da imagem", style=discord.TextStyle.short, required=False)
            self.add_item(self.url)

        async def on_submit(self, interaction: discord.Interaction):
            url = self.url.value.strip()
            if url == "":
                self.parent.embed.set_image(url=None)
            else:
                self.parent.embed.set_image(url=url)
            await self.parent.update_message(interaction)

    class EditThumbnailModal(discord.ui.Modal, title="Editar URL da thumbnail (imagem pequena)"):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            self.url = discord.ui.TextInput(label="URL da thumbnail", style=discord.TextStyle.short, required=False)
            self.add_item(self.url)

        async def on_submit(self, interaction: discord.Interaction):
            url = self.url.value.strip()
            if url == "":
                self.parent.embed.set_thumbnail(url=None)
            else:
                self.parent.embed.set_thumbnail(url=url)
            await self.parent.update_message(interaction)

    class EditCorModal(discord.ui.Modal, title="Editar cor do embed (hexadecimal)"):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            self.hex = discord.ui.TextInput(label="Cor hexadecimal (ex: #ff0000)", style=discord.TextStyle.short, required=True, max_length=7)
            self.add_item(self.hex)

        async def on_submit(self, interaction: discord.Interaction):
            cor = self.hex.value.strip()
            if cor.startswith("#"):
                cor = cor[1:]
            try:
                cor_int = int(cor, 16)
                if cor_int < 0 or cor_int > 0xFFFFFF:
                    raise ValueError()
            except:
                await interaction.response.send_message("Cor inválida. Use hexadecimal válido.", ephemeral=True)
                return

            self.parent.embed.color = cor_int
            await self.parent.update_message(interaction)

    @discord.ui.button(
        label="Editar Título",
        style=discord.ButtonStyle.primary,
        emoji="<:title:1401244870466863235>"
    )
    async def editar_titulo(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(self.EditTituloModal(self))

    @discord.ui.button(
        label="Editar Descrição",
        style=discord.ButtonStyle.primary,
        emoji="<:Icon_Channel_Channels:1314237864082542643>"
    )
    async def editar_descricao(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(self.EditDescricaoModal(self))

    @discord.ui.button(
        label="Editar Imagem",
        style=discord.ButtonStyle.secondary,
        emoji="<:Icon_Channel_Media:1401245079968157897>"
    )
    async def editar_imagem(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(self.EditImagemModal(self))

    @discord.ui.button(
        label="Editar Thumbnail",
        style=discord.ButtonStyle.secondary,
        emoji="<:Icon_Channel_Media:1401245079968157897>"
    )
    async def editar_thumbnail(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(self.EditThumbnailModal(self))

    @discord.ui.button(
        label="Editar Cor",
        style=discord.ButtonStyle.success,
        emoji="<:palette:1401245570240221346>"
    )
    async def editar_cor(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(self.EditCorModal(self))

    @discord.ui.button(
        label="Enviar Embed",
        style=discord.ButtonStyle.green,
        emoji="<:send:1401246032142008412>"
    )
    async def enviar_embed(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Embed enviado!", ephemeral=True)
        await self.interaction.channel.send(embed=self.embed)
        self.stop()

    async def update_message(self, interaction: discord.Interaction):
        try:
            await interaction.response.edit_message(embed=self.embed, view=self)
        except discord.errors.InteractionResponded:
            await interaction.followup.edit_message(self.message.id, embed=self.embed, view=self)

class EmbedCreator(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="embed", description="💬｜Cria um embed interativo.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def embed(self, interaction: discord.Interaction):
        view = EmbedBuilderView(self.bot, interaction)
        await view.start()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EmbedCreator(bot))
