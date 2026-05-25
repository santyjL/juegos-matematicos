from enum import Enum
from turtle import right, width

class Colores(Enum):
    BACKGROUND="#eef"
    COLOR_COMPONENTES ="#fff" 

body = dict[str, str](
    background=Colores.BACKGROUND.value,
    margin=0,
    min_height="100vh",
    min_width="100vw",
)

icon_style = dict[str, str](
    color= Colores.COLOR_COMPONENTES.value,
    display="inline-block",
    width="24px",
    height="24px",
    margin="20px 10px",
)

navbar__component = dict[str, str](
    background="#48e",
    min_width="100%",
    max_height="60px",
    position="fixed",
    top=0,
    left=0,
    margin=0,
    z_index=40
)