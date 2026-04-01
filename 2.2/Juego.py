# ==============================
# VARIABLES
# ==============================
import flet as ft
import random

opciones = ["Piedra", "Papel", "Tijeras"]


# ==============================
# FUNCIÓN PRINCIPAL
# ==============================
def main(page: ft.Page):

    page.title = "Piedra, Papel o Tijeras"
    page.window_width = 400
    page.window_height = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Puntaje almacenado en diccionario (sin usar global)
    puntaje = {
        "jugador": 0,
        "computadora": 0
    }

    # --------------------------
    # CONTROLES
    # --------------------------
    titulo = ft.Text(
        "Piedra, Papel o Tijeras",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    resultado_texto = ft.Text(
        "Elige una opción para comenzar",
        size=16,
        text_align=ft.TextAlign.CENTER
    )

    puntaje_texto = ft.Text(
        "Puntaje → Tú: 0 | Computadora: 0",
        size=16,
        weight=ft.FontWeight.BOLD
    )

    # --------------------------
    # FUNCIÓN JUGAR
    # --------------------------
    def jugar(eleccion_jugador):

        eleccion_computadora = random.choice(opciones)

        if eleccion_jugador == eleccion_computadora:
            resultado = "¡Empate!"

        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijeras") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
             (eleccion_jugador == "Tijeras" and eleccion_computadora == "Papel"):

            resultado = "¡Ganaste!"
            puntaje["jugador"] += 1
        else:
            resultado = "Perdiste..."
            puntaje["computadora"] += 1

        resultado_texto.value = (
            f"Tú: {eleccion_jugador}\n"
            f"Computadora: {eleccion_computadora}\n\n"
            f"{resultado}"
        )

        puntaje_texto.value = (
            f"Puntaje → Tú: {puntaje['jugador']} | "
            f"Computadora: {puntaje['computadora']}"
        )

        page.update()

    # --------------------------
    # FUNCIÓN REINICIAR
    # --------------------------
    def reiniciar(e):
        puntaje["jugador"] = 0
        puntaje["computadora"] = 0

        resultado_texto.value = "Elige una opción para comenzar"
        puntaje_texto.value = "Puntaje → Tú: 0 | Computadora: 0"

        page.update()

    # --------------------------
    # FUNCIÓN SALIR (compatible web y desktop)
    # --------------------------
    def salir(e):
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text("Juego terminado", size=26, weight=ft.FontWeight.BOLD),
                    ft.Text("Gracias por jugar", size=18)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # --------------------------
    # BOTONES
    # --------------------------
    botones = ft.Row(
        [
            ft.ElevatedButton("Piedra", on_click=lambda e: jugar("Piedra")),
            ft.ElevatedButton("Papel", on_click=lambda e: jugar("Papel")),
            ft.ElevatedButton("Tijeras", on_click=lambda e: jugar("Tijeras")),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    boton_reiniciar = ft.ElevatedButton(
        "Reiniciar Juego",
        on_click=reiniciar
    )

    boton_salir = ft.ElevatedButton(
        "Salir",
        on_click=salir
    )

    # --------------------------
    # DISEÑO
    # --------------------------
    page.add(
        ft.Column(
            [
                titulo,
                resultado_texto,
                puntaje_texto,
                botones,
                boton_reiniciar,
                boton_salir
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )


# ==============================
# INICIAR APP
# ==============================
ft.app(target=main)
