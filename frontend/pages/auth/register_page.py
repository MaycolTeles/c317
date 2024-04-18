import flet as ft

from components import Gap, InputTextField
from navigation import Routes
from styles import colors


class RegisterPage():
    def __init__(self, page: ft.Page):
        self._page = page

    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.background,
            content=self._get_content()
        )

    def _get_content(self):
        return ft.Column(
            [
                ft.Container(
                    ft.Image(
                        src="iws_logo.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    height=140,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    self._get_register_content(),
                    bgcolor=colors.primary_color,
                    padding=30,
                    border_radius=ft.BorderRadius(20, 20, 0, 0),
                    expand=True,
                ),
            ]
        )

    def _get_register_content(self):
        access_text = ft.Text(
            value="Cadastre-se",
            color=colors.white,
            weight=ft.FontWeight.BOLD,
            size=20,
        )
        form = self._get_register_form()

        return ft.Column(
            [
                access_text,
                form
            ]
        )

    def _get_register_form(self):

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

        form = ft.Column(
            [
                ft.Text("Digite seu nome completo:", color=colors.white),
                InputTextField(label="Nome"),
                Gap(5),
                ft.Text("Digite seu e-mail:", color=colors.white),
                InputTextField(
                    label="E-mail",
                    keyboard_type=ft.KeyboardType.EMAIL,
                ),
                Gap(5),
                ft.Text("Digite sua senha:", color=colors.white),
                InputTextField(
                    label="Senha",
                    is_password_field=True,
                ),
                Gap(5),
                ft.Text("Confirme sua senha:", color=colors.white),
                InputTextField(
                    label="Senha",
                    is_password_field=True,
                ),
            ]
        )

        buttons = ft.Column(
            controls=[
                ft.ElevatedButton(
                    content=ft.Text("CRIAR CADASTRO", weight=ft.FontWeight.BOLD),
                    width=300,
                    height=50,
                    style=login_button_style,
                    on_click=self._handle_register
                ),
                Gap(10),
                ft.ElevatedButton(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Gap(20),
                            ft.Text("Já tem cadastro? Acesse", weight=ft.FontWeight.BOLD),
                            ft.Icon(ft.icons.ARROW_FORWARD),
                        ]
                    ),
                    width=300,
                    height=50,
                    style=register_button_style,
                    on_click=self._handle_already_registered,
                ),
            ]
        )

        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                form,
                Gap(20),
                buttons
            ],
        )

    def _handle_register(self, event: ft.ControlEvent):
        print("TODO: IMPLEMENTAR REGISTAR USUÁRIO")

    def _handle_already_registered(self, event: ft.ControlEvent):
        self._page.go(Routes.LOGIN_PAGE.value)
