class RegisterPage(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def build(self):
        column = ft.Column(
            controls=[
                # logo
                ft.Container(
                    bgcolor="white",
                    height=300,
                ),
                ft.Container(
                    content=self._get_content(),
                    bgcolor="blue",
                    padding=20,
                )
            ],
            spacing=10,
            scroll=ft.ScrollMode.ALWAYS,
        )

        # logo = ft.logo


        return column

    def _get_content(self):
        access_text = ft.Text(value="ACESSAR", color="white", weight=ft.FontWeight.BOLD)
        form = self._get_login_form()

        content = ft.Column(
            controls=[access_text, form],
            width=900,
            height=400,
        )

        return content

    def _get_login_form(self):
        return ft.Column(
            content=[
                ft.Text("Digite seu e-mail", colors="white")
            ]
        )
