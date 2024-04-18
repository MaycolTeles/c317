
import flet as ft


class Gap(ft.Container):

    def __init__(self, size: int = 20, **kwargs):
        super().__init__(**kwargs)
        self.size = size

    def build(self):
        return ft.Container(
            height=self.size,
            width=self.size
        )
