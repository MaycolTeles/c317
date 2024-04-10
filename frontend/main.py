import flet as ft

from pages import HomePage


def main(page: ft.Page):
    page.title = "C317 - Frontend"

    app = HomePage()

    page.add(app)

ft.app(target=main)
