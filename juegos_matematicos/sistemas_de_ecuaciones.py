import reflex as rx

from juegos_matematicos.estado_algebra import AlgebraState
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


def fila_ecuacion(ecuacion: str) -> rx.Component:
    return rx.box(
        rx.text(ecuacion, size="5", weight="medium"),
        style={**caja_ecuacion_style, "width": "auto", "padding": "12px 20px"},
    )


def fila_respuesta(indice: int) -> rx.Component:
    fruta = AlgebraState.frutas[indice]
    return rx.box(
        rx.hstack(
            rx.box(fruta, style=caja_ecuacion_style),
            rx.box("=", style=caja_ecuacion_style),
            rx.input(
                placeholder="?",
                value=AlgebraState.respuestas[indice],
                on_change=lambda v: AlgebraState.set_respuesta(v, indice),
                type="number",
                style={**caja_ecuacion_style, "width": "70px"},
            ),
            align="center",
        ),
    )


def box_juego() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading("Ecuaciones y Frutas", style=heading_style),
                rx.spacer(),
                rx.badge(
                    f"⏱ {AlgebraState.tiempo_restante}s",
                    size="2",
                    color_scheme="red",
                ),
                width="100%",
                align="center",
            ),
            rx.hstack(
                rx.vstack(
                    rx.foreach(
                        AlgebraState.ecuaciones,
                        fila_ecuacion,
                    ),
                    spacing="3",
                    flex="1",
                ),
                rx.vstack(
                    rx.foreach(
                        AlgebraState.indices_frutas,
                        fila_respuesta,
                    ),
                    spacing="3",
                    background="#fff",
                    border_radius="20px",
                    padding="16px",
                    flex="1",
                ),
                width="100%",
                align="start",
                spacing="6",
            ),
            rx.button(
                "Comprobar",
                on_click=AlgebraState.comprobar,
                style=button_play_style,
            ),
            spacing="5",
            width="100%",
        ),
        style=caja_de_juego_style,
    )


@rx.page(route=Routers.ECUACIONES_Y_FRUTAS.value, on_load=AlgebraState.iniciar)
def ecuaciones_y_frutas() -> rx.Component:
    return rx.container(
        navbar(),
        box_juego(),
        modal_resultado(AlgebraState, "Ecuaciones y Frutas"),
        style=body,
    )
