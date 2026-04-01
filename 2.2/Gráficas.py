import matplotlib.pyplot as plt
import flet as ft
import base64
from io import BytesIO
import random

# convertir grafica matplotlib a imagen base64
def fig_to_src(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"


# --- FUNCIONES DE GRÁFICAS ---

def generar_grafica_barras():
    productos = ["A", "B", "C", "D"]
    ventas = [15, 30, 45, 10]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.bar(productos, ventas)
    ax.set_title("Ventas por Producto")

    return fig_to_src(fig)


def generar_grafica_lineas():
    meses = ["Ene","Feb","Mar","Abr","May"]
    rendimiento = [10,25,18,40,35]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.plot(meses, rendimiento, marker="o")
    ax.set_title("Tendencia de Rendimiento")
    ax.grid(True)

    return fig_to_src(fig)


def generar_grafica_dispersion():

    x = [i for i in range(20)]
    y = [random.randint(10,50) for _ in range(20)]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.scatter(x,y)
    ax.set_title("Muestreo de Sensores")

    return fig_to_src(fig)


def generar_grafica_circular():

    categorias = ["Tecnología","Salud","Educación","Otros"]
    valores = [40,25,20,15]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.pie(valores, labels=categorias, autopct="%1.1f%%")
    ax.set_title("Distribución por Categoría")

    return fig_to_src(fig)


def main(page: ft.Page):

    page.title = "Graficas"
    page.theme_mode = ft.ThemeMode.LIGHT

    header = ft.Text("Gráficas", size=24, weight="bold")

    tablero = ft.GridView(
        expand=True,
        runs_count=2,
        spacing=20,
        run_spacing=20,
        child_aspect_ratio=1.5
    )

    # --- GRAFICAS ---
    img1 = ft.Image(src=generar_grafica_barras())
    img2 = ft.Image(src=generar_grafica_lineas())
    img3 = ft.Image(src=generar_grafica_dispersion())
    img4 = ft.Image(src=generar_grafica_circular())

    contenedor_1 = ft.Container(img1, border=ft.border.all(1,"black12"), border_radius=10, padding=10)
    contenedor_2 = ft.Container(img2, border=ft.border.all(1,"black12"), border_radius=10, padding=10)
    contenedor_3 = ft.Container(img3, border=ft.border.all(1,"black12"), border_radius=10, padding=10)
    contenedor_4 = ft.Container(img4, border=ft.border.all(1,"black12"), border_radius=10, padding=10)

    tablero.controls.extend([
        contenedor_1,
        contenedor_2,
        contenedor_3,
        contenedor_4
    ])

    page.add(header, ft.Divider(), tablero)


ft.app(target=main)
