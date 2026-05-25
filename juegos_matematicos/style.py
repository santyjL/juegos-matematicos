from tkinter import N
from typing import Any


from enum import Enum
from turtle import right, width

class Colores(Enum):
    BACKGROUND="#eef"
    COLOR_COMPONENTES ="#fff" 
    COLOR_CONTENEDORES ="#48e"

    COLOR_TITULOS = "#48e"
    COLOR_TEXTO = "#fff"

    TEXT_SHADOW_TITULOS = "0 0 10PX #48f"

    BOX_SHADOW = "0 0 40px 10px #48e"

class Tamaños(Enum):
    TITULO = "2.3em"

heading_style = dict[str, str] (
    color=Colores.COLOR_TITULOS.value,
    font_size=Tamaños.TITULO,
    margin_bottom="20px",
    text_shadow=Colores.TEXT_SHADOW_TITULOS.value
    
)

body = dict[str, str](
    background=Colores.BACKGROUND.value,
    margin=0,
    min_height="100vh",
    min_width="100%",
)

icon_style = dict[str, str](
    color= Colores.COLOR_COMPONENTES.value,
    display="inline-block",
    width="24px",
    height="24px",
    margin="20px 10px",
)

navbar__component = dict[str, str](
    background=Colores.COLOR_CONTENEDORES.value,
    min_width="100%",
    max_width="100%",
    max_height="60px",
    position="fixed",
    top=0,
    left=0,
    margin=0,
    z_index=40
)

contenedor_juegos_hover = dict[str,str](
    box_shadow= Colores.BOX_SHADOW.value,
)

contenedor__juegos__style = dict[str,str](
    margin= "10px",
    padding= "10px",
    border= f"2px solid {Colores.COLOR_CONTENEDORES.value}",
    border_radius= "10px",
    position= "relative",
    background= Colores.COLOR_CONTENEDORES.value,
    max_width= "50%",
    min_height= "40%",
    box_shadow= "0 0 0 0 #fff",
    box_sizing="border-box",
    transition= "box-shadow 1s ease",
    _hover= contenedor_juegos_hover,
)


list_reglas = dict[str, str](
    text_wrap="balance",
    margin="20px 2px"
)

link_play_hover=dict[str,str](
    background=Colores.COLOR_COMPONENTES.value,
    text_color=Colores.COLOR_TITULOS.value,
    text_decoration=None,
    border="3px solid #08e"
)

button_play_style=dict[str,str](
    border_radius="10px",
    padding="10px",
    margin="20px 10px",
    border="3px solid #fff",
    color=Colores.COLOR_TEXTO.value,
    _hover=link_play_hover
)

link_style=dict[str,str](
    color="#fff",
    weight="bold",
    width="100%",
    display="inline-block",
    _hover={"color" : "#48e"}
)