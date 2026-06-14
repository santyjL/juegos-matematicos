import reflex as rx

from juegos_matematicos.style import navbar__component, navbar_title_style


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.heading(
                "JUEGOMATEMATICA",
                justify="start",
                style=navbar_title_style,
            ),
            color="#fff",
            href="/",
            width="100%",
            _hover={"color": "#fff"},
        ),
        style=navbar__component,
    )
