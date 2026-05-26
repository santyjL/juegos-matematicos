import reflex as rx

from juegos_matematicos.style import icon_style, navbar__component


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.heading(
                "JUEGOMATEMATICA",
                justify="start",
                margin="20px 10px",
            ),
            color="#fff",
            href="/",
            width="100%",
            _hover={"color": "#fff"},
        ),
        style=navbar__component,
    )
