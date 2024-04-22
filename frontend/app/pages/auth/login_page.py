import flet as ft

from api.auth import AuthAPI
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

        self._email_text_field = InputTextField(
            label="E-mail",
            keyboard_type=ft.KeyboardType.EMAIL,
        )
        self._password_text_field = InputTextField(
            label="Senha",
            is_password_field=True,
        )

        return ft.Column(
            [
                ft.Text("Digite seu e-mail:", color=colors.white),
                self._email_text_field,
                Gap(20),
                ft.Text("Digite sua senha:", color=colors.white),
                self._password_text_field,
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
        is_form_valid = self._validate_login_form()
        if not is_form_valid:
            return

        email: str = self._email_text_field.value  # type: ignore
        password: str = self._password_text_field.value  # type: ignore
        
        try:
            AuthAPI.login_user(
                email=email,
                password=password
            )

        except Exception as e:
            print("ERRO: ", e)
            self._dlg_modal = ft.AlertDialog(
                modal=True,
                open=True,
                title=ft.Text("Erro ao fazer login"),
                content=ft.Text("Ocorreu um erro ao fazer login. Tente novamente mais tarde."),
                actions_alignment=ft.MainAxisAlignment.END,
                actions=[
                    ft.TextButton("Ok", on_click=self._close_dlg),
                ],
            )

            self._page.dialog = self._dlg_modal
            self._page.update()
            return

        self._page.go(Routes.HOME_PAGE.value)

    def _close_dlg(self, event: ft.ControlEvent):
        self._dlg_modal.open = False
        self._page.update()

    def _validate_login_form(self):
        email = self._email_text_field.value
        password = self._password_text_field.value

        form_is_valid = True
        if not email:
            self._email_text_field.error_text = "Por favor, insira um e-mail válido!"
            form_is_valid = False
        else:
            self._email_text_field.error_text = ""

        if not password:
            self._password_text_field.error_text = "Por favor, insira uma senha válida!"
            form_is_valid = False
        else:
            self._password_text_field.error_text = ""

        self._page.update()

        return form_is_valid
