
import flet as ft

from styles import colors


class ChatMessageCard:
    def __init__(self, message: str):
        self._message = message

    def get_content(self):
        return ft.Card(
            ft.Container(
                ft.Text(
                    self._message,
                    max_lines=60,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
                padding=20,
            ),
            color=colors.secondary_color,
            margin=ft.Margin(left=5, right=5, top=10, bottom=10),
            expand=True,
            expand_loose=True,
        )
