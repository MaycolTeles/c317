import flet as ft

from pages import RegisterPage


def main(page: ft.Page):
    page.title = "C317 - Frontend"
    page.spacing = 0

    app = RegisterPage()

    page.add(app)


ft.app(target=main)
