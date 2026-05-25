import reflex as rx
from juegos_matematicos.style import (body,contenedor__juegos__style, heading_style,)
from juegos_matematicos.routes import Routers
from juegos_matematicos.navbar import navbar

@rx.page(route=Routers.ECUACIONES_Y_FRUTAS.value)
def ecuaciones_y_frutas() -> rx.components:
    return rx.container(
        navbar(),
        style=body
    )