from turtle import width
import reflex as rx
from juegos_matematicos.style import navbar__component,icon_style

def link_icon(link:str, icon_name:str) -> rx.Component:
    return rx.link(
        rx.icon(icon_name),
        href=link,
        style=icon_style
    )

def navbar() -> rx.Component:
    return rx.hstack(
            rx.heading(
                "JUEGOMATEMATICA",
                justify="start",
                margin="20px 10px",
                width="80%"
            ),
            rx.box(
                link_icon(link="http://localhost:3000", icon_name="calendar"),
                link_icon(link="http://localhost:3000", icon_name="calendar"),
                link_icon(link="http://localhost:3000", icon_name="calendar"),
                link_icon(link="http://localhost:3000", icon_name="calendar"),
                link_icon(link="http://localhost:3000", icon_name="calendar"),
                justify="end",
            ),
            style=navbar__component
        ),
        