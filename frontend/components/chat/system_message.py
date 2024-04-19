
import flet as ft

from .message import ChatMessageCard
from styles import colors


class SystemMessage:
    def __init__(self, message: str):
        self._message = message

    def get_content(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.Icon(
                    ft.icons.SUPPORT_AGENT_OUTLINED,
                    color=colors.primary_color,
                    size=30,
                ),
                ChatMessageCard(self._message).get_content(),
            ]
        )
