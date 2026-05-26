import reflex as rx

from juegos_matematicos.estado_sucesiones import SucesionesState
from juegos_matematicos.modales import modal_resultado
from juegos_matematicos.navbar import navbar
from juegos_matematicos.routes import Routers
from juegos_matematicos.style import (
    body,
    button_play_style,
    caja_de_juego_style,
    caja_ecuacion_style,
    heading_style,
)


def celda_secuencia(indice: int) -> rx.Component:
    return rx.cond(
        SucesionesState.es_oculto[indice],
        rx.box("?", style=caja_ecuacion_style),
        rx.box(
            SucesionesState.secuencia[indice],
            style=caja_ecuacion_style,
        ),
    )


def fila_respuesta_oculta(indice: int) -> rx.Component:
    return rx.hstack(
        rx.text(f"Respuesta {indice + 1}:", color="#fff"),
        rx.input(
            placeholder="?",
            value=SucesionesState.respuestas[indice],
            on_change=lambda v: SucesionesState.set_respuesta(v, indice),
            type="number",
            style={**caja_ecuacion_style, "width": "80px"},
        ),
        align="center",
        spacing="3",
    )


def box_juego_sucesiones() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading("Encuentra el patrón", style=heading_style),
                rx.spacer(),
                rx.badge(
                    f"⏱ {SucesionesState.tiempo_restante}s",
                    size="2",
                    color_scheme="red",
                ),
                width="100%",
                align="center",
            ),
            rx.text(
                "Completa los tres últimos números de la secuencia.",
                color="#fff",
            ),
            rx.hstack(
                rx.foreach(
                    SucesionesState.indices_secuencia,
                    celda_secuencia,
                ),
                spacing="2",
                wrap="wrap",
                justify="center",
            ),
            rx.vstack(
                rx.foreach(
                    SucesionesState.indices_respuestas,
                    fila_respuesta_oculta,
                ),
                spacing="3",
                width="100%",
                align="start",
            ),
            rx.button(
                "Comprobar",
                on_click=SucesionesState.comprobar,
                style=button_play_style,
            ),
            spacing="5",
            width="100%",
        ),
        style=caja_de_juego_style,
    )


@rx.page(route=Routers.ENCUENTRA_EL_PATRON.value, on_load=SucesionesState.iniciar)
def encuentra_el_patron() -> rx.Component:
    return rx.container(
        navbar(),
        box_juego_sucesiones(),
        modal_resultado(SucesionesState, "Encuentra el patrón"),
        style=body,
    )
