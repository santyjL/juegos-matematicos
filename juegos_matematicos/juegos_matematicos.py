"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from juegos_matematicos.style import (body,contenedor__juegos__style, heading_style,
                                        list_reglas, button_play_style, link_style)
from juegos_matematicos.navbar import navbar

def contenedor_juegos (regla1:str,regla2:str,
                        regla3:str,tiempo:str,
                        enlace:str) -> rx.Component:
    return rx.box(
        rx.heading(
            "Ecuaciones y Frutas 🍏"
        ),
        rx.text(
            "Reglas",
            weight="bold"
        ),
        rx.list.unordered(
            rx.list.item(regla1),
            rx.list.item(regla2),
            rx.list.item(regla3),
            rx.list.item(tiempo),
            text_align="start",
            style=list_reglas
        ),
        rx.box(
            rx.link(
                "iniciar juego",
                href=enlace,
                style=link_style
            ),
            style=button_play_style,
        ),
        style=contenedor__juegos__style,
    )

def juegos_descripcion() ->rx.Component:
    return rx.center(
        rx.container(
            rx.heading("Juegos matematicos", style=heading_style),
            rx.hstack(
                contenedor_juegos(
                    regla1="Se presentan ecuaciones con frutas (🍊,🍎,🍓,etc)",
                    regla2="Cada figura representa un numero desconocido",
                    regla3="Debes usar las ecuaciones para descubrir su valor",
                    tiempo="Solo tienes 20segundos para encontrar la respuesta correcta",
                    enlace="https://youtube.com"
                ),
                contenedor_juegos(
                regla1="Se presentan ecuaciones con frutas (🍊,🍎,🍓,etc)",
                regla2="Cada figura representa un numero desconocido",
                regla3="Debes usar las ecuaciones para descubrir su valor",
                tiempo="Solo tienes 20segundos para encontrar la respuesta correcta",
                enlace="https://youtube.com"
            )
            ),
            margin="100px 0",
            justify="center",
            text_align="center",
        )
    )
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        juegos_descripcion(),
        style=body
        
    )


app = rx.App()
app.add_page(index)
