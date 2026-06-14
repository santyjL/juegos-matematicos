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
    game_header_style,
    heading_style2,
    page_container_style,
    timer_box_style,
)

ecuacion_style = {
    **caja_ecuacion_style,
    "width": "auto",
    "min_width": "auto",
    "height": "auto",
    "min_height": rx.breakpoints(initial="40px", sm="46px", md="50px"),
    "padding": rx.breakpoints(initial="8px 12px", sm="10px 16px", md="12px 20px"),
}

input_respuesta_style = {
    **caja_ecuacion_style,
    "width": rx.breakpoints(initial="56px", sm="64px", md="70px"),
    "min_width": rx.breakpoints(initial="56px", sm="64px", md="70px"),
}


def fila_ecuacion(ecuacion: str) -> rx.Component:
    return rx.box(
        rx.text(
            ecuacion,
            size=rx.breakpoints(initial="3", sm="4", md="5"),
            weight="medium",
        ),
        style=ecuacion_style,
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
                style=input_respuesta_style,
            ),
            align="center",
            justify=rx.breakpoints(initial="center", sm="start"),
            width="100%",
        ),
        width="100%",
    )


def box_juego() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.heading("Ecuaciones y Frutas", style=heading_style2),
                rx.box(
                    rx.center(
                        rx.text(
                            f"⏱ {AlgebraState.tiempo_restante}s",
                            weight="bold",
                            font_size=rx.breakpoints(initial="1.2em", sm="1.5em"),
                        ),
                    ),
                    style=timer_box_style,
                ),
                direction=rx.breakpoints(initial="column", sm="row"),
                style=game_header_style,
            ),
            rx.flex(
                rx.vstack(
                    rx.foreach(
                        AlgebraState.ecuaciones,
                        fila_ecuacion,
                    ),
                    spacing="3",
                    flex="1",
                    width="100%",
                    align=rx.breakpoints(initial="center", lg="start"),
                ),
                rx.vstack(
                    rx.foreach(
                        AlgebraState.indices_frutas,
                        fila_respuesta,
                    ),
                    spacing="3",
                    background="#fff",
                    border_radius=rx.breakpoints(initial="14px", sm="20px"),
                    padding=rx.breakpoints(initial="12px", sm="16px"),
                    flex="1",
                    width="100%",
                    align=rx.breakpoints(initial="center", lg="start"),
                ),
                direction=rx.breakpoints(initial="column", lg="row"),
                width="100%",
                align="stretch",
                gap=rx.breakpoints(initial="16px", lg="24px"),
            ),
            rx.button(
                "Comprobar",
                on_click=AlgebraState.comprobar,
                style=button_play_style,
                width=rx.breakpoints(initial="100%", sm="auto"),
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
        style={**body, **page_container_style},
    )
