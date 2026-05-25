import reflex as rx
from juegos_matematicos.style import (body,contenedor__juegos__style, heading_style,)
from juegos_matematicos.routes import Routers
from juegos_matematicos.navbar import navbar

@rx.page(route=Routers.ENCUENTRA_EL_PATRON.value)
def encuentra_el_patron() -> rx.components:
    return rx.container(
        navbar(),
        style=body
    )