import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timezone, timedelta

BRAZIL_TZ = timezone(timedelta(hours=-3))  # UTC-3

class UserInfo(commands.Cog):
    """Comando /user_info para exibir informações detalhadas de um usuário."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ===== Helper methods =====
    @staticmethod
    def _format_datetime(dt: datetime) -> str:
        """Formata datetimes em formato dd/mm/AAAA HH:MM."""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        dt_brt = dt.astimezone(BRAZIL_TZ)
        return dt_brt.strftime("%d/%m/%Y %H:%M")

    # ===== Slash command =====
    @app_commands.command(name="user_info", description="ℹ️｜Mostra informações sobre um usuário")
    @app_commands.describe(usuario="Usuário a obter informações. Deixe vazio para você.")
    async def user_info(self, interaction: discord.Interaction, usuario: discord.Member | None = None):
        member = usuario or interaction.user  # Usa o membro fornecido ou quem chamou o comando

        # Monta o embed
        embed = discord.Embed(
            title=f"Informações de {member.display_name}",
            color=member.color if isinstance(member, discord.Member) else discord.Color.blue(),
            timestamp=datetime.now(timezone.utc)
        )

        # Avatar grande no topo e pequeno na lateral
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_image(url=member.display_avatar.replace(size=512).url)

        # Campos básicos
        embed.add_field(name="👤 Nome", value=f"{member.name}#{member.discriminator}", inline=True)
        embed.add_field(name="🏷️ Apelido", value=member.nick or "Nenhum", inline=True)
        embed.add_field(name="🆔 ID", value=str(member.id), inline=False)

        # Datas
        embed.add_field(
            name="📅 Conta criada em",
            value=self._format_datetime(member.created_at),
            inline=True,
        )
        if isinstance(member, discord.Member) and member.joined_at:
            embed.add_field(
                name="📌 Entrou no servidor em",
                value=self._format_datetime(member.joined_at),
                inline=True,
            )
        else:
            embed.add_field(name="📌 Entrou no servidor em", value="Informação indisponível", inline=True)

        # Cargo mais alto
        if isinstance(member, discord.Member):
            embed.add_field(name="🥇 Cargo mais alto", value=member.top_role.mention, inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=False)


async def setup(bot: commands.Bot):
    await bot.add_cog(UserInfo(bot))
