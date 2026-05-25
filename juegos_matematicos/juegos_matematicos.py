"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from juegos_matematicos.style import body
from juegos_matematicos.navbar import navbar

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        style=body
        
    )


app = rx.App()
app.add_page(index)
