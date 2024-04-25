
import flet as ft

from .message import ChatMessageCard
from styles import colors


class SystemMessage:
    def __init__(self, message: str):
        self._message = message

    def get_content(self):
        return ft.Container(
            padding=ft.Padding(right=100, left=0, top=0, bottom=0),
            content=ft.Row(
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
        )
