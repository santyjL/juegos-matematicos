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
    game_header_style,
    heading_style2,
    page_container_style,
    timer_box_style,
)

input_respuesta_style = {
    **caja_ecuacion_style,
    "width": rx.breakpoints(initial="64px", sm="72px", md="80px"),
    "min_width": rx.breakpoints(initial="64px", sm="72px", md="80px"),
}


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
        rx.text(f"R{indice + 1} -->", color="#fff"),
        rx.input(
            placeholder="?",
            value=SucesionesState.respuestas[indice],
            on_change=lambda v: SucesionesState.set_respuesta(v, indice),
            type="number",
            style=input_respuesta_style,
        ),
        align="center",
        spacing="3",
        width="100%",
        justify=rx.breakpoints(initial="center", sm="start"),
    )


def box_juego_sucesiones() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.heading("Encuentra el patrón", style=heading_style2),
                rx.box(
                    rx.center(
                        rx.text(
                            f"⏱ {SucesionesState.tiempo_restante}s",
                            font_size=rx.breakpoints(initial="1.2em", sm="1.5em"),
                        )
                    ),
                    style=timer_box_style,
                ),
                direction=rx.breakpoints(initial="column", sm="row"),
                style=game_header_style,
            ),
            rx.text(
                "Completa los tres últimos números de la secuencia.",
                color="#fff",
                weight="bold",
                font_size=rx.breakpoints(initial="1em", sm="1.15em", md="1.3em"),
                text_align=rx.breakpoints(initial="center", sm="left"),
            ),
            rx.flex(
                rx.foreach(
                    SucesionesState.indices_secuencia,
                    celda_secuencia,
                ),
                gap=rx.breakpoints(initial="4px", sm="8px"),
                wrap="wrap",
                justify="center",
                width="100%",
            ),
            rx.vstack(
                rx.foreach(
                    SucesionesState.indices_respuestas,
                    fila_respuesta_oculta,
                ),
                spacing="3",
                width="100%",
                align=rx.breakpoints(initial="center", sm="start"),
            ),
            rx.button(
                "Comprobar",
                on_click=SucesionesState.comprobar,
                style=button_play_style,
                width=rx.breakpoints(initial="100%", sm="auto"),
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
        style={**body, **page_container_style},
    )
