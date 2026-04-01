import flet as ft

class Usuario:
    def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
        self.nombre = nombre
        self.rol = rol
        self.color_borde = color_borde


class TarjetaPerfil(ft.Container):
    def __init__(self, usuario, pagina):
        super().__init__()

        self.usuario = usuario
        self.pagina = pagina   # ← cambiamos page por pagina

        self.content = ft.Column(
            controls=[
                ft.Text(usuario.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(usuario.rol, italic=True),
                ft.ElevatedButton("Ver perfil", on_click=self.saludar)
            ],
            tight=True
        )

        self.border = ft.border.all(2, usuario.color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    def saludar(self, e):
        print(f"Interactuando con {self.usuario.nombre}")


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Componentes Definidos por el Usuario"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.iniciar()

    def iniciar(self):

        usuario1 = Usuario("Ana Garcia", "Desarrolladora Senior", ft.Colors.PURPLE)
        usuario2 = Usuario("Carlos Ruiz", "Arquitecto de Software", ft.Colors.PINK)

        tarjeta1 = TarjetaPerfil(usuario1, self.page)
        tarjeta2 = TarjetaPerfil(usuario2, self.page)

        self.page.add(
            ft.Text("Lista de Usuarios", size=30, weight="bold"),
            ft.Row([tarjeta1, tarjeta2], alignment=ft.MainAxisAlignment.CENTER)
        )


def main(page: ft.Page):
    App(page)


ft.app(target=main)
