import json
import threading

import flet as ft
from websockets.sync.client import connect

from api import UserMessageAPI, SessionAPI, WEBSOCKET_URL
from components import SystemMessage, UserMessage, InputTextField
from navigation.routes import Routes
from styles import colors


class ChatBotPage:
    _session_id: str

    def __init__(self, page: ft.Page):

        self._create_new_chat_section()

        self._page = page

        self._page.appbar = ft.AppBar(
            ft.IconButton(
                ft.icons.ARROW_BACK,
                on_click=self._handle_back_button,
            ),
            title=ft.Text("Atendimento IWS", style=ft.TextStyle(color=colors.white, size=24)),
            bgcolor=colors.primary_color,
            center_title=True,
            toolbar_height=80,
        )
        self._page.update()

    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.background_grey,
            content=self._get_content(),
        )

    def _create_new_chat_section(self):
        session_id = SessionAPI.create()
        self._session_id = session_id

        uri = f"{WEBSOCKET_URL}/{session_id}/"
        self._websocket = connect(uri)

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
            height=600,
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
        self._input_field.update()

    def _handle_on_blur(self, event: ft.ControlEvent):
        self._input_field.hint_text = "Digite qual a sua dúvida..."
        self._input_field.update()

    def _handle_back_button(self, event: ft.ControlEvent):
        self._page.go(Routes.HOME_PAGE.value)

    def _handle_send_message(self, event: ft.ControlEvent):
        msg = self._input_field.value
        if not msg:
            return

        send_message_thread = threading.Thread(target=self._send_message_to_backend, args=(msg,))
        send_message_thread.start()

        self._input_field.value = ""
        self._input_field.update()

        message = UserMessage(msg).get_content()

        self._chat_history.controls.append(message)
        self._chat_history.update()

    def _send_message_to_backend(self, msg: str):
        self._websocket.send(json.dumps({'message': msg}))
        UserMessageAPI.create(msg, self._session_id)
