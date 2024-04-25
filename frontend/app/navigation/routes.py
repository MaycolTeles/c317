from enum import Enum


class Routes(Enum):
    INDEX_PAGE = "/"
    WELCOME_PAGE = "/bem-vindo"
    HOME_PAGE = "/home"
    LOGIN_PAGE = "/login"
    REGISTER_PAGE = "/registrar"
    CHATBOT_PAGE = "/atendimento"
    SUPPORT_PAGE = "/suporte"
    PASSWORD_RECOVERY_PAGE = "/recuperar-senha"
