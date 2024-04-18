import flet as ft

from components import Gap


class RegisterPage(ft.Container):
    def __init__(self):
        super().__init__()

        self.content = ft.Container(
            ft.Column(
                [
                    # logo
                    ft.Container(
                        bgcolor="white",
                        height=400,
                    ),
                    ft.Container(
                        self._get_content(),
                        bgcolor="blue",
                        padding=20,
                        height=400
                    ),
                ],
                spacing=0,
            ),
            expand=True,
        )

    def _get_content(self):
        access_text = ft.Text(value="Acesse", color="white", weight=ft.FontWeight.BOLD)
        form = self._get_login_form()

        content = ft.Column(
            [access_text, form],
        )

        return content

    def _get_login_form(self):

        register_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(
                radius=10,
            ),
            color="white",
            bgcolor="blue",
        )
        login_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color="blue",
            bgcolor="white",
        )

        buttons = ft.Row(
            [
                ft.ElevatedButton(
                    text="Cadastrar",
                    width=150,
                    height=50,
                    style=register_button_style,
                    on_click=_handle_register
                ),
                Gap(10),
                ft.ElevatedButton(
                    text="Entrar",
                    width=150,
                    height=50,
                    style=login_button_style,
                    on_click=_handle_login
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )

        return ft.Column(
            [
                ft.Text("Digite seu e-mail:", color="white"),
                ft.TextField(label="E-mail", keyboard_type=ft.KeyboardType.EMAIL),
                Gap(20),
                ft.Text("Digite sua senha:", color="white"),
                ft.TextField(label="Senha", password=True, can_reveal_password=True),
                ft.Container(
                    ft.TextButton(
                        text="Esqueci minha senha",
                        on_click=_handle_forgot_password,
                        style=ft.ButtonStyle(
                            color="white",
                        ),
                    ),
                    alignment=ft.alignment.center_right,
                ),
                Gap(20),
                buttons
            ],
        )


def _handle_forgot_password():
    print("Forgot password clicked!")


def _handle_register():
    print("Register clicked!")


def _handle_login():
    print("Login clicked!")
