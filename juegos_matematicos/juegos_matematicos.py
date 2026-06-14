"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from juegos_matematicos.style import (
    body,
    button_play_style,
    contenedor__juegos__style,
    games_grid_style,
    heading_style,
    link_style,
    list_reglas,
    page_container_style,
)
from juegos_matematicos.routes import Routers
from juegos_matematicos.navbar import navbar
from juegos_matematicos.sistemas_de_ecuaciones import ecuaciones_y_frutas
from juegos_matematicos.sucesiones import encuentra_el_patron

def contenedor_juegos (titulo:str,
                        regla1:str,regla2:str,
                        regla3:str,tiempo:str,
                        enlace:str) -> rx.Component:
    return rx.box(
        rx.heading(
            titulo
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

def juegos_descripcion() -> rx.Component:
    return rx.center(
        rx.container(
            rx.heading("Juegos matematicos", style=heading_style),
            rx.flex(
                contenedor_juegos(
                    titulo="Ecuaciones y Frutas 🍏",
                    regla1="Se presentan ecuaciones con frutas (🍊,🍎,🍓,etc)",
                    regla2="Cada figura representa un numero desconocido",
                    regla3="Debes usar las ecuaciones para descubrir su valor",
                    tiempo="Solo tienes 20segundos para encontrar la respuesta correcta",
                    enlace=Routers.ECUACIONES_Y_FRUTAS.value,
                ),
                contenedor_juegos(
                    titulo="Encuentra el patron",
                    regla1="Se muestra una secuencia de numeros",
                    regla2="Debes identificar el patron que sigue",
                    regla3="encuentra el siguiente numero",
                    tiempo="Solo tienes 30segundos para completar la secuencia",
                    enlace=Routers.ENCUENTRA_EL_PATRON.value,
                ),
                direction=rx.breakpoints(initial="column", md="row"),
                style=games_grid_style,
            ),
            margin=rx.breakpoints(initial="72px 0 32px", sm="100px 0"),
            justify="center",
            text_align="center",
            style=page_container_style,
        ),
        width="100%",
    )
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        juegos_descripcion(),
        style={**body, **page_container_style},
    )

app = rx.App()
app.add_page(index)
app.add_page(ecuaciones_y_frutas)
app.add_page(encuentra_el_patron)
