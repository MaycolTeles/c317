import flet as ft

from api.auth import AuthAPI
from components import Gap, InputTextField
from navigation import Routes
from styles import colors


class RegisterPage:
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

        self._name_text_field = InputTextField(label="Nome")
        self._email_text_field = InputTextField(
            label="E-mail",
            keyboard_type=ft.KeyboardType.EMAIL,
        )
        self._password_text_field = InputTextField(
            label="Senha",
            is_password_field=True,
        )
        self._password_confirmation_text_field = InputTextField(
            label="Confirme sua senha",
            is_password_field=True,
        )

        form = ft.Column(
            [
                ft.Text("Digite seu nome completo:", color=colors.white),
                self._name_text_field,
                Gap(5),
                ft.Text("Digite seu e-mail:", color=colors.white),
                self._email_text_field,
                Gap(5),
                ft.Text("Digite sua senha:", color=colors.white),
                self._password_text_field,
                Gap(5),
                ft.Text("Confirme sua senha:", color=colors.white),
                self._password_confirmation_text_field,
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
        is_form_valid = self._validate_register_form()
        if not is_form_valid:
            return

        username: str = self._name_text_field.value  # type: ignore
        email: str = self._email_text_field.value  # type: ignore
        password: str = self._password_text_field.value  # type: ignore

        try:
            AuthAPI.register_user(
                username=username,
                email=email,
                password=password
            )

        except Exception as e:
            print("ERRO: ", e)
            self._dlg_modal = ft.AlertDialog(
                modal=True,
                open=True,
                title=ft.Text("Erro ao registrar"),
                content=ft.Text("Ocorreu um erro ao tentar registrar o usuário. Tente novamente mais tarde."),
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

    def _handle_already_registered(self, event: ft.ControlEvent):
        self._page.go(Routes.LOGIN_PAGE.value)

    def _validate_register_form(self):
        name = self._name_text_field.value
        email = self._email_text_field.value
        password = self._password_text_field.value
        password_confirmation = self._password_confirmation_text_field.value

        form_is_valid = True
        if not name:
            self._name_text_field.error_text = "Por favor, insira um nome válido!"
            form_is_valid = False
        else:
            self._name_text_field.error_text = ""

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

        if password != password_confirmation:
            self._password_confirmation_text_field.error_text = "As senhas não coincidem!"
            form_is_valid = False
        else:
            self._password_confirmation_text_field.error_text = ""

        self._page.update()

        return form_is_valid
