import flet as ft

from components import Gap
from navigation import Routes
from styles import colors


class HomePage():
    def __init__(self, page: ft.Page):
        self._page = page

    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.background,
            content=self._get_content(),
        )

    def _get_content(self):
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
                ft.Text(
                    "Seja bem vindo! Faça login para continuar.",
                    color=colors.primary_color,
                    weight=ft.FontWeight.BOLD,
                    size=16,
                ),
                Gap(200),
                ft.Container(
                    padding=20,
                    content=self._get_buttons(),
                )
            ]
        )

    def _get_buttons(self):
        button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.white,
            bgcolor=colors.primary_color,
        )

        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.ElevatedButton(
                    content=ft.Text("CADASTRAR", weight=ft.FontWeight.BOLD),
                    width=150,
                    height=50,
                    style=button_style,
                    on_click=self._handle_register
                ),
                Gap(10),
                ft.ElevatedButton(
                    content=ft.Text("FAZER LOGIN", weight=ft.FontWeight.BOLD),
                    width=150,
                    height=50,
                    style=button_style,
                    on_click=self._handle_login
                ),
            ],
        )

    def _handle_register(self, event: ft.ControlEvent):
        self._page.go(Routes.REGISTER_PAGE.value)

    def _handle_login(self, event: ft.ControlEvent):
        self._page.go(Routes.LOGIN_PAGE.value)
