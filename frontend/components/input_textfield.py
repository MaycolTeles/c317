
import flet as ft

from styles import colors


class InputTextField(ft.TextField):
    def __init__(self, label: str, keyboard_type: ft.KeyboardType = ft.KeyboardType.TEXT, is_password_field: bool = False):
        super().__init__(
            bgcolor=colors.textfield_background,
            keyboard_type=keyboard_type,
            label=label,
            password=is_password_field,
            can_reveal_password=is_password_field,
            border_color=colors.white,
        )
