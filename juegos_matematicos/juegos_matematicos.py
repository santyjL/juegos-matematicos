"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        
    )


app = rx.App()
app.add_page(index)
