
import flet as ft

from navigation.routes import Routes
import pages


class Router:
    routes_map = {
        Routes.INDEX_PAGE.value: pages.WelcomePage,
        Routes.WELCOME_PAGE.value: pages.WelcomePage,
        Routes.HOME_PAGE.value: pages.HomePage,
        Routes.LOGIN_PAGE.value: pages.LoginPage,
        Routes.REGISTER_PAGE.value: pages.RegisterPage,
        Routes.CHATBOT_PAGE.value: pages.ChatBotPage,
        Routes.SUPPORT_PAGE.value: pages.SupportPage,
        Routes.PASSWORD_RECOVERY_PAGE.value: pages.PasswordRecoveryPage,
    }

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.body = ft.Container(pages.WelcomePage(page).get_content())

    def on_route_change(self, route: ft.RouteChangeEvent):
        page = self.routes_map[route.route](self.page)
        self.body.content = page.get_content()

        self.page.appbar = None
        self.page.floating_action_button = None
        self.body.update()
