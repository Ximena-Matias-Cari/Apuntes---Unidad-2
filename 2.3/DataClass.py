import flet as ft
from dataclasses import dataclass
#definicion del componente personalizado


@dataclass
class TarjetaPerfil:
    nombre : str
    rol : str
    color_borde : str =  ft.Colors.BLUE
    
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(self.nombre, weight=ft.FontWeight.BOLD, size=20),
                    ft.Text(self.rol, italic=True),
                    ft.ElevatedButton("Ver perfil", on_click=self.saludar)
                ],
                tight=True
            ),
            border=ft.border.all(2, self.color_borde),
            padding=10,
            border_radius=10,
            width=200
        )

    def saludar(self, e):
        print(f"Interactuando con {self.nombre}")

def main(page: ft.Page):
    page.title = "Unidad 2: Componentes definidos por el usuario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Intanciando nuestros componentes personalizados
    usuario1 = TarjetaPerfil("Ana García", "Desarrolladora senior", ft.Colors.GREEN)
    usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software")

    page.add(
        ft.Text("Lista de usuarios", size=30, weight="bold"),
        ft.Row([usuario1.build(), usuario2.build()], alignment=ft.MainAxisAlignment.CENTER)
    )
ft.app(target=main)
