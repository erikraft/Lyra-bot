from __future__ import annotations

import discord
from discord.ext import commands
from discord import app_commands, Interaction, ui, ButtonStyle, Member, TextChannel, Guild
from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING

from config import id_do_servidor, ID_CANAL_LOGS, ID_CANAL_MOD, link_apelacao

COR_BAN = 0xff4c4c
COR_KICK = 0xff944c
COR_MUTE = 0x4c6aff


def gerar_view_apelacao():
    view = discord.ui.View()
    view.add_item(discord.ui.Button(
        label="Essa ação foi injusta?",
        url=link_apelacao,
        style=discord.ButtonStyle.link
    ))
    return view

class ModPainel(ui.View):
    def __init__(self, bot: commands.Bot, usuario: Member) -> None:
        super().__init__(timeout=180)
        self.bot = bot
        self.usuario = usuario

    @discord.ui.button(
        label="Banir",
        style=discord.ButtonStyle.danger,
        emoji="<:Icon_BanMember:1401246654438576260>"
    )
    async def banir(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(BanModal(self.bot, self.usuario))

    @discord.ui.button(
        label="Kick",
        style=discord.ButtonStyle.danger,
        emoji="<:Icon_Member_Kick:1401246895107604552>"
    )
    async def kickar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(KickModal(self.bot, self.usuario))

    @discord.ui.button(
        label="Mute",
        style=discord.ButtonStyle.secondary,
        emoji="<:Icon_Timeout:1401246976921571448>"
    )
    async def mutar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(MuteModal(self.bot, self.usuario))

class BanModal(ui.Modal, title="Banir Usuário"):
    def __init__(self, bot: commands.Bot, usuario: Member) -> None:
        super().__init__()
        self.bot = bot
        self.usuario = usuario
        self.motivo = discord.ui.TextInput(
            label="Motivo do banimento",
            style=discord.TextStyle.paragraph,
            placeholder="Descreva o motivo da punição...",
            required=True,
            max_length=500
        )
        self.add_item(self.motivo)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        motivo = self.motivo.value
        try:
            await self.usuario.ban(reason=motivo)

            try:
                embed_dm = discord.Embed(
                    title="<:IconR_ban:1314237924702945344> Você foi banido",
                    description=f"Motivo: {motivo}",
                    color=COR_BAN
                )
                embed_dm.set_footer(text="Adeus.")
                await self.usuario.send(embed=embed_dm, view=gerar_view_apelacao())
            except:
                pass

            canal_logs = self.bot.get_channel(ID_CANAL_LOGS)
            mod_logs = self.bot.get_channel(ID_CANAL_MOD)
            if canal_logs:
                embed_log = discord.Embed(
                    title="<:IconR_ban:1314237924702945344> Banimento aplicado",
                    description=f"{self.usuario.mention} foi banido por {interaction.user.mention}",
                    color=COR_BAN,
                    timestamp=datetime.utcnow()
                )
                embed_log.add_field(name="Motivo", value=motivo, inline=False)
                await canal_logs.send(embed=embed_log)
                await mod_logs.send(embed=embed_log)

            embed_resp = discord.Embed(
                description=f"{self.usuario.mention} foi banido com sucesso.",
                color=COR_BAN
            )
            await interaction.response.send_message(embed=embed_resp, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Erro ao banir: {e}", ephemeral=True)

class KickModal(ui.Modal, title="Expulsar Usuário"):
    def __init__(self, bot: commands.Bot, usuario: Member) -> None:
        super().__init__()
        self.bot = bot
        self.usuario = usuario
        self.motivo = discord.ui.TextInput(
            label="Motivo da expulsão",
            style=discord.TextStyle.paragraph,
            placeholder="Descreva o motivo da punição...",
            required=True,
            max_length=500
        )
        self.add_item(self.motivo)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        motivo = self.motivo.value
        try:
            await self.usuario.kick(reason=motivo)

            try:
                embed_dm = discord.Embed(
                    title="<:Icon_Member_Kick:1401246895107604552> Você foi expulso",
                    description=f"Motivo: {motivo}",
                    color=COR_KICK
                )
                await self.usuario.send(embed=embed_dm, view=gerar_view_apelacao())
            except:
                pass

            canal_logs = self.bot.get_channel(ID_CANAL_LOGS)
            mod_logs = self.bot.get_channel(ID_CANAL_MOD)
            if canal_logs:
                embed_log = discord.Embed(
                    title="<:Icon_Member_Kick:1401246895107604552> Expulsão aplicada",
                    description=f"{self.usuario.mention} foi expulso por {interaction.user.mention}",
                    color=COR_KICK,
                    timestamp=datetime.utcnow()
                )
                embed_log.add_field(name="Motivo", value=motivo, inline=False)
                await canal_logs.send(embed=embed_log)

            embed_resp = discord.Embed(
                description=f"{self.usuario.mention} foi expulso com sucesso.",
                color=COR_KICK
            )
            await interaction.response.send_message(embed=embed_resp, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Erro ao expulsar: {e}", ephemeral=True)

class MuteModal(ui.Modal, title="Mutar Usuário"):
    def __init__(self, bot: commands.Bot, usuario: Member) -> None:
        super().__init__()
        self.bot = bot
        self.usuario = usuario

        self.motivo = discord.ui.TextInput(
            label="Motivo do mute",
            style=discord.TextStyle.paragraph,
            placeholder="Motivo da punição...",
            required=True,
            max_length=500
        )
        self.tempo = discord.ui.TextInput(
            label="Duração do mute (horas)",
            style=discord.TextStyle.short,
            placeholder="Número de horas",
            required=True,
            max_length=3
        )
        self.add_item(self.motivo)
        self.add_item(self.tempo)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        motivo = self.motivo.value
        try:
            horas = float(self.tempo.value)
        except ValueError:
            await interaction.response.send_message("Duração inválida. Use um número válido em horas.", ephemeral=True)
            return

        duracao = timedelta(hours=horas)

        try:
            timeout_expira_em = discord.utils.utcnow() + duracao

            await self.usuario.edit(timed_out_until=timeout_expira_em, reason=motivo)

            try:
                embed_dm = discord.Embed(
                    title="<:Icon_Timeout:1401246976921571448> Você foi silenciado",
                    description=f"Motivo: {motivo}\nDuração: {horas} horas",
                    color=COR_MUTE
                )
                embed_dm.set_footer(text="Você pode apelar da decisão.")
                await self.usuario.send(embed=embed_dm, view=gerar_view_apelacao())
            except:
                pass

            canal_logs = self.bot.get_channel(ID_CANAL_LOGS)
            mod_logs = self.bot.get_channel(ID_CANAL_MOD)
            if canal_logs:
                embed_log = discord.Embed(
                    title="<:Icon_Timeout:1401246976921571448> Timeout aplicado",
                    description=f"{self.usuario.mention} foi silenciado por {interaction.user.mention}",
                    color=COR_MUTE,
                    timestamp=datetime.utcnow()
                )
                embed_log.add_field(name="Motivo", value=motivo, inline=False)
                embed_log.add_field(name="Duração", value=f"{horas} horas", inline=True)
                await canal_logs.send(embed=embed_log)

            embed_resp = discord.Embed(
                description=f"{self.usuario.mention} foi silenciado por {horas} horas.",
                color=COR_MUTE
            )
            await interaction.response.send_message(embed=embed_resp, ephemeral=True)

        except Exception as e:
            await interaction.response.send_message(f"Erro ao aplicar mute: {e}", ephemeral=True)

class Mod(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="painel_mod", description="🛡️｜Abre o painel de moderação para um usuário.")
    @app_commands.describe(usuario="Usuário para abrir o painel de moderação")
    @app_commands.checks.has_permissions(administrator=True)
    async def abrir_painel_mod(self, interaction: Interaction, usuario: Member) -> None:
        embed = discord.Embed(
            title="<:Icon_Moderation:1401248956406693988> Painel de Moderação",
            description=f"Ações disponíveis para moderar {usuario.mention}",
            color=0xffcc00,
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=usuario.display_avatar.url)

        embed.add_field(name="👤 Usuário", value=str(usuario), inline=True)
        embed.add_field(name="🏷️ Apelido", value=usuario.nick or "Nenhum", inline=True)
        embed.add_field(name="🆔 ID", value=str(usuario.id), inline=False)
        embed.add_field(name="📅 Conta criada", value=usuario.created_at.strftime('%d/%m/%Y %H:%M'), inline=True)
        embed.add_field(name="📌 Entrou no servidor", value=usuario.joined_at.strftime('%d/%m/%Y %H:%M'), inline=True)

        view = ModPainel(self.bot, usuario)  # Usa self.bot ao invés de bot
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Mod(bot))
