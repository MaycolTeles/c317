
import flet as ft


class Gap(ft.Container):

    def __init__(self, size: int = 20, **kwargs):
        super().__init__(**kwargs)
        self.height = size
        self.width = size
