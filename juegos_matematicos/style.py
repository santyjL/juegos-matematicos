from enum import Enum
from reflex_base.breakpoints import Breakpoints
from typing import Any

import reflex as rx


class Colores(Enum):
    BACKGROUND = "#eef"
    COLOR_COMPONENTES = "#fff"
    COLOR_CONTENEDORES = "#48e"

    COLOR_TITULOS = "#48e"
    COLOR_TITULOS2 = "#fff"
    COLOR_TEXTO = "#fff"

    TEXT_SHADOW_TITULOS = "0 0 10PX #48f"

    BOX_SHADOW = "0 0 40px 10px #48e"


class Tamaños(Enum):
    TITULO = "2.3em"


# Espaciado responsivo compartido
NAVBAR_HEIGHT = rx.breakpoints(initial="52px", sm="60px")
PAGE_OFFSET_TOP = rx.breakpoints(initial="68px", sm="80px")

heading_style = dict[str, str | Breakpoints | Breakpoints[str, Any]](
    color=Colores.COLOR_TITULOS.value,
    font_size=rx.breakpoints(initial="1.5em", sm="2em", md=Tamaños.TITULO.value),
    margin_bottom=rx.breakpoints(initial="12px", sm="20px"),
    text_shadow=Colores.TEXT_SHADOW_TITULOS.value,
)

heading_style2 = dict[str, str | Breakpoints | Breakpoints[str, Any]](
    color=Colores.COLOR_TITULOS2.value,
    font_size=rx.breakpoints(initial="1.35em", sm="1.8em", md=Tamaños.TITULO.value),
    margin_bottom=rx.breakpoints(initial="8px", sm="20px"),
    text_shadow=Colores.TEXT_SHADOW_TITULOS.value,
    text_align=rx.breakpoints(initial="center", sm="left"),
)

body = dict[str, str | int](
    background=Colores.BACKGROUND.value,
    margin=0,
    min_height="100vh",
    min_width="100%",
    width="100%",
    overflow_x="hidden",
)

icon_style = dict[str, str | Breakpoints | Breakpoints[str, Any]](
    color=Colores.COLOR_COMPONENTES.value,
    display="inline-block",
    width="24px",
    height="24px",
    margin=rx.breakpoints(initial="12px 8px", sm="20px 10px"),
)

navbar__component = dict[str, str | Breakpoints | Breakpoints[str, Any] | int](
    background=Colores.COLOR_CONTENEDORES.value,
    min_width="100%",
    max_width="100%",
    min_height=NAVBAR_HEIGHT,
    position="fixed",
    top=0,
    left=0,
    margin=0,
    padding=rx.breakpoints(initial="0 12px", sm="0 16px"),
    z_index=40,
    box_sizing="border-box",
)

navbar_title_style = dict[str, Breakpoints | Breakpoints[str, Any]](
    margin=rx.breakpoints(initial="10px 0", sm="20px 10px"),
    font_size=rx.breakpoints(initial="1.1em", sm="1.4em", md="1.6em"),
)

contenedor_juegos_hover = dict[str, str](
    box_shadow=Colores.BOX_SHADOW.value,
)

contenedor__juegos__style = dict[str, Breakpoints | Breakpoints[str, Any] | str | dict[str, str]](
    margin=rx.breakpoints(initial="0", sm="10px"),
    padding=rx.breakpoints(initial="16px", sm="20px"),
    border=f"2px solid {Colores.COLOR_CONTENEDORES.value}",
    border_radius="10px",
    position="relative",
    background=Colores.COLOR_CONTENEDORES.value,
    width=rx.breakpoints(initial="100%", md="calc(50% - 12px)"),
    max_width=rx.breakpoints(initial="100%", md="520px"),
    flex=rx.breakpoints(initial="1 1 100%", md="1 1 calc(50% - 12px)"),
    min_height=rx.breakpoints(initial="auto", sm="40%"),
    box_shadow="0 0 0 0 #fff",
    box_sizing="border-box",
    transition="box-shadow 1s ease",
    _hover=contenedor_juegos_hover,
)

list_reglas = dict[str, str | Breakpoints | Breakpoints[str, Any]](
    text_wrap="balance",
    margin=rx.breakpoints(initial="12px 0", sm="20px 2px"),
    font_size=rx.breakpoints(initial="0.95em", sm="1em"),
)

link_play_hover = dict[str, str](
    background="#000",
    text_color=Colores.COLOR_TITULOS.value,
    text_decoration=None,
    border="3px solid #08e",
)

button_play_style = dict[str, str | Breakpoints | Breakpoints[str, Any]](
    border_radius="10px",
    padding=rx.breakpoints(initial="14px 20px", sm="10px 16px"),
    margin=rx.breakpoints(initial="16px 0 0", sm="20px 10px"),
    border="3px solid #fff",
    color=Colores.COLOR_TEXTO.value,
    min_height="44px",
    min_width=rx.breakpoints(initial="100%", sm="120px"),
    cursor="pointer",
    font_size=rx.breakpoints(initial="1em", sm="1em"),
)

link_style = dict[str, str | dict[str, str]](
    color="#fff",
    weight="bold",
    width="100%",
    display="inline-block",
    text_align="center",
    _hover={"color": "#48e"},
)

caja_de_juego_style = dict[str, Breakpoints | Breakpoints[str, Any] | str](
    width=rx.breakpoints(initial="100%", sm="96%", md="90%"),
    max_width="960px",
    height=rx.breakpoints(initial="auto", lg="70vh"),
    min_height=rx.breakpoints(initial="auto", lg="400px"),
    margin="auto",
    padding=rx.breakpoints(initial="14px", sm="16px", md="20px"),
    margin_top=PAGE_OFFSET_TOP,
    margin_bottom=rx.breakpoints(initial="24px", sm="32px"),
    border_radius=rx.breakpoints(initial="14px", sm="20px"),
    align_items="center",
    background=Colores.COLOR_CONTENEDORES.value,
    box_sizing="border-box",
)

caja_ecuacion_style = dict[str, str | Breakpoints | Breakpoints[str, Any]](
    background=Colores.BACKGROUND.value,
    width=rx.breakpoints(initial="40px", sm="46px", md="50px"),
    height=rx.breakpoints(initial="40px", sm="46px", md="50px"),
    min_width=rx.breakpoints(initial="40px", sm="46px", md="50px"),
    min_height=rx.breakpoints(initial="40px", sm="46px", md="50px"),
    font_size=rx.breakpoints(initial="1.25em", sm="1.5em", md="2em"),
    color=Colores.COLOR_CONTENEDORES.value,
    margin=rx.breakpoints(initial="3px", sm="5px", md="7px"),
    text_align="center",
    display="flex",
    align_items="center",
    justify_content="center",
    border_radius="6px",
    box_sizing="border-box",
)

timer_box_style = dict[str, Breakpoints | Breakpoints[str, Any] | str](
    width=rx.breakpoints(initial="88px", sm="100px"),
    height=rx.breakpoints(initial="44px", sm="50px"),
    background="#f009",
    border_radius="20px",
    padding=rx.breakpoints(initial="6px", sm="10px"),
    flex_shrink="0",
)

game_header_style = dict[str, str | Breakpoints | Breakpoints[str, Any]](
    width="100%",
    gap=rx.breakpoints(initial="12px", sm="16px"),
    align_items="center",
    justify_content=rx.breakpoints(initial="center", sm="space-between"),
    flex_wrap="wrap",
)

modal_content_style = dict[str, Breakpoints | Breakpoints[str, Any] | str](
    max_width=rx.breakpoints(initial="min(95vw, 400px)", sm="420px"),
    width=rx.breakpoints(initial="95vw", sm="auto"),
    background="#48e",
    padding=rx.breakpoints(initial="16px", sm="24px"),
    margin="auto"
    
)

modal_actions_style = dict[str, Breakpoints | Breakpoints[str, Any] | str](
    gap=rx.breakpoints(initial="12px", sm="16px"),
    margin_top="16px",
    flex_direction=rx.breakpoints(initial="column", sm="row"),
    width="100%",

)

page_container_style = dict[str, Breakpoints | Breakpoints[str, Any] | str](
    padding=rx.breakpoints(initial="0 12px", sm="0 20px", md="0 24px"),
    max_width="1200px",
    width="100%",
    box_sizing="border-box",
)

games_grid_style = dict[str, str](
    width="100%",
    gap=rx.breakpoints(initial="16px", md="20px"),
    justify_content="center",
    align_items="stretch",
    flex_wrap="wrap",
)
