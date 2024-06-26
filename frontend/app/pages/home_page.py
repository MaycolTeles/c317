import flet as ft

from components import Gap, InputTextField
from navigation import Routes
from styles import colors


class HomePage:
    def __init__(self, page: ft.Page):
        self._page = page

        self._page.appbar = ft.AppBar(
            bgcolor=colors.primary_color,
            actions=[
                ft.IconButton(
                    ft.icons.SETTINGS,
                    on_click=self._handle_open_settings,
                )
            ]
        )
        self._page.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.SUPPORT_AGENT,
            on_click=self._handle_start_chatbot,
            bgcolor=colors.primary_color,
        )
        self._page.update()

    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.background,
            content=self._get_content(),
        )

    def _get_content(self):
        button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.white,
            bgcolor=colors.primary_color,
        )

        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    ft.Image(
                        src="iws_logo.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    height=250,
                    alignment=ft.alignment.center,
                ),
                Gap(100),
                ft.Text(
                    "APLICAÇÃO IWS",
                    color=colors.primary_color,
                    weight=ft.FontWeight.BOLD,
                    size=16,
                ),
                Gap(100),
                ft.ElevatedButton(
                    content=ft.Text("Conectar a um chat", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    width=200,
                    height=50,
                    style=button_style,
                    on_click=self._handle_connect_to_chat
                ),
                Gap(20),
            ]
        )

    def _handle_start_chatbot(self, event: ft.ControlEvent):
        self._page.go(Routes.CHATBOT_PAGE.value)

    def _handle_open_settings(self, event: ft.ControlEvent):
        print("OPEN SETTINGS")
        self._page.go(Routes.WELCOME_PAGE.value)

    def _handle_connect_to_chat(self, event: ft.ControlEvent):
        self._page.go(Routes.SUPPORT_PAGE.value)
