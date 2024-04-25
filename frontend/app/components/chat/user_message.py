
import flet as ft

from .message import ChatMessageCard
from styles import colors


class UserMessage:
    def __init__(self, message: str):
        self._message = message

    def get_content(self):
        return ft.Container(
                padding=ft.Padding(right=0, left=100, top=0, bottom=0),
                content=ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    ChatMessageCard(self._message).get_content(),
                    ft.Icon(
                        ft.icons.PERSON,
                        color=colors.primary_color,
                        size=30,
                    ),
                ]
            )
        )
