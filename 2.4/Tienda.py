import flet as ft

# ----------------------------
# DATOS DE PRODUCTOS
# ----------------------------
productos = [
    {"id":1,"nombre":"Laptop Gamer","descripcion":"Laptop con alto rendimiento","precio":25000,"ruta_imagen":"laptop.jpg"},
    {"id":2,"nombre":"Audífonos Bluetooth","descripcion":"Audio inalámbrico de alta calidad","precio":1200,"ruta_imagen":"audifonos.jpg"},
    {"id":3,"nombre":"Smartphone","descripcion":"Teléfono con cámara de alta resolución","precio":15000,"ruta_imagen":"celular.jpg"},
    {"id":4,"nombre":"Tablet","descripcion":"Ideal para estudio y entretenimiento","precio":8000,"ruta_imagen":"tablet.jpg"},
    {"id":5,"nombre":"Reloj","descripcion":"Reloj con diseño de flores, elegante y práctico","precio":1500,"ruta_imagen":"reloj.jpg"}
]


# ----------------------------
# COMPONENTE REUTILIZABLE
# ----------------------------
class TarjetaProducto(ft.Container):

    def __init__(self, producto):
        super().__init__()

        self.width = 250
        self.padding = 10
        self.border_radius = 15
        self.bgcolor = ft.Colors.WHITE
        self.shadow = ft.BoxShadow(blur_radius=8, color=ft.Colors.BLACK12)

        self.content = ft.Column(
            spacing=8,
            controls=[

                ft.Image(
                    src=producto["ruta_imagen"],
                    width=230,
                    height=150,
                    fit="cover"
                ),

                ft.Text(
                    producto["nombre"],
                    size=18,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    producto["descripcion"],
                    size=12,
                    color=ft.Colors.GREY
                ),

                ft.Text(
                    f"${producto['precio']}",
                    size=16,
                    color=ft.Colors.GREEN,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),

                        ft.ElevatedButton(
                            "Agregar al carrito",
                            icon=ft.Icons.SHOPPING_CART
                        )
                    ]
                )
            ]
        )


# ----------------------------
# APP PRINCIPAL
# ----------------------------
def main(page: ft.Page):

    page.title = "TekoStore"
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.scroll = "auto"

    tarjetas = []

    for producto in productos:
        tarjetas.append(TarjetaProducto(producto))

    page.add(

        ft.Text(
            "TechStore",
            size=35,
            weight=ft.FontWeight.BOLD
        ),

        ft.Text(
            "Catálogo de productos",
            size=18
        ),

        ft.ResponsiveRow(
            controls=tarjetas
        )
    )


# ----------------------------
# EJECUTAR
# ----------------------------
ft.app(target=main, assets_dir="assets")
