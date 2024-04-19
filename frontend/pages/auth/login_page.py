import flet as ft

from components import Gap, InputTextField
from navigation import Routes
from styles import colors


class LoginPage:
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
            [
                ft.Container(height=100),
                ft.Container(
                    ft.Image(
                        src="iws_logo.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    height=250,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    self._get_login_content(),
                    bgcolor=colors.primary_color,
                    padding=30,
                    border_radius=ft.BorderRadius(20, 20, 0, 0),
                    expand=True,
                ),
            ]
        )

    def _get_login_content(self):
        access_text = ft.Text(
            value="Acesse",
            color=colors.white,
            weight=ft.FontWeight.BOLD,
            size=20,
        )
        form = self._get_login_form()

        content = ft.Column(
            [access_text, Gap(10), form],
        )

        return content

    def _get_login_form(self):

        register_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.white,
            bgcolor=colors.primary_color,
            side=ft.border.BorderSide(width=2, color=colors.white),
        )
        login_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.primary_color,
            bgcolor=colors.white,
        )

        buttons = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Text("CADASTRAR", weight=ft.FontWeight.BOLD),
                    width=150,
                    height=50,
                    style=register_button_style,
                    on_click=self._handle_register
                ),
                Gap(10),
                ft.ElevatedButton(
                    content=ft.Text("ENTRAR", weight=ft.FontWeight.BOLD),
                    width=150,
                    height=50,
                    style=login_button_style,
                    on_click=self._handle_login
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )

        return ft.Column(
            [
                ft.Text("Digite seu e-mail:", color=colors.white),
                InputTextField(
                    label="E-mail",
                    keyboard_type=ft.KeyboardType.EMAIL,
                ),
                Gap(20),
                ft.Text("Digite sua senha:", color=colors.white),
                InputTextField(
                    label="Senha",
                    is_password_field=True,
                ),
                ft.Container(
                    ft.TextButton(
                        text="Esqueci minha senha",
                        on_click=self._handle_forgot_password,
                        style=ft.ButtonStyle(
                            color=colors.white,
                        ),
                    ),
                    alignment=ft.alignment.center_right,
                ),
                Gap(20),
                buttons,
            ],
        )

    def _handle_forgot_password(self, event: ft.ControlEvent):
        print("TODO: IMPLEMENTAR RECUPERAÇÃO DE SENHA")

    def _handle_register(self, event: ft.ControlEvent):
        self._page.go(Routes.REGISTER_PAGE.value)

    def _handle_login(self, event: ft.ControlEvent):
        print("TODO: IMPLEMENTAR VALIDACAO LOGIN")
        self._page.go(Routes.HOME_PAGE.value)
