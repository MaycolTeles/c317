import flet as ft

from navigation.router import Router
from styles import colors


def main(page: ft.Page):
    page.title = "Aplicativo IWS"
    page.padding = 0
    page.bgcolor = colors.background

    router = Router(page)
    page.on_route_change = router.on_route_change
    page.add(router.body)


ft.app(target=main)
