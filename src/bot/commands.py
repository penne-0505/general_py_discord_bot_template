from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import discord


if TYPE_CHECKING:
    from bot.client import BotClient

LOGGER = logging.getLogger(__name__)


async def register_commands(client: "BotClient") -> None:
    """クライアントのアプリケーションコマンドを登録する。"""

    tree = client.tree

    @tree.command(name="ping", description="Botの応答速度を確認します。")
    async def ping_command(interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Pong!")


__all__ = ["register_commands"]
