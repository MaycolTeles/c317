import flet as ft

from components import SystemMessage, UserMessage, InputTextField, Gap
from navigation.routes import Routes
from styles import colors


class SupportPage:
    def __init__(self, page: ft.Page):
        self._page = page

        title = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Suporte Técnico IWS",
                    style=ft.TextStyle(color=colors.white, size=22)
                ),
                Gap(1),
                ft.Text(
                    "Percebemos que sua dúvida ainda não foi sanada.",
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(color=colors.white, size=12)
                ),
                ft.Text(
                    "Direcionamos você para nosso atendimento especializado.",
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(color=colors.white, size=12)
                )
            ]
        )

        self._page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.icons.ARROW_BACK,
                on_click=self._handle_back_button,
            ),
            leading_width=40,
            title=title,
            bgcolor=colors.primary_color,
            center_title=True,
            toolbar_height=150,
        )
        self._page.update()

    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.background_grey,
            content=self._get_content(),
        )

    def _get_content(self):
        self._input_field = InputTextField(
            hint_text="Digite qual a sua dúvida...",
            keyboard_type=ft.KeyboardType.TEXT,
            multiline=True,
            min_lines=1,
            max_lines=3,
            on_submit=self._handle_send_message,
            shift_enter=True,
            on_focus=self._handle_on_focus,
            on_blur=self._handle_on_blur,
            suffix=ft.IconButton(
                ft.icons.SEND,
                icon_color=colors.secondary_color,
                on_click=self._handle_send_message,
            )
        )

        self._chat_history = ft.ListView(
            height=530,
            padding=20,
            controls=[
                SystemMessage("Olá, como eu posso te ajudar hoje?").get_content(),
            ],
        )

        return ft.Column(
            [
                self._chat_history,
                ft.Container(
                    self._input_field,
                    bgcolor=colors.primary_color,
                    padding=ft.Padding(top=40, bottom=40, left=30, right=30),
                    border_radius=ft.BorderRadius(20, 20, 0, 0),
                    expand=True,
                ),
            ]
        )

    def _handle_on_focus(self, event: ft.ControlEvent):
        self._input_field.hint_text = ""
        self._page.update()

    def _handle_on_blur(self, event: ft.ControlEvent):
        self._input_field.hint_text = "Digite qual a sua dúvida..."
        self._page.update()

    def _handle_back_button(self, event: ft.ControlEvent):
        self._page.go(Routes.HOME_PAGE.value)

    def _handle_send_message(self, event: ft.ControlEvent):
        input = self._input_field.value
        if not input:
            return

        self._input_field.value = ""

        message = UserMessage(input).get_content()

        self._chat_history.controls.append(message)
        self._page.update()

        # TODO: SEND MESSAGE TO BACKEND
