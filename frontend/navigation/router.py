
import flet as ft


from navigation.routes import Routes
import pages


class Router:
    routes_map = {
        Routes.HOME_PAGE.value: pages.HomePage,
        Routes.LOGIN_PAGE.value: pages.LoginPage,
        Routes.REGISTER_PAGE.value: pages.RegisterPage,
    }

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.body = ft.Container(pages.HomePage(page).get_content())

    def on_route_change(self, route: ft.RouteChangeEvent):
        page = self.routes_map[route.route](self.page)
        self.body.content = page.get_content()
        self.body.update()
