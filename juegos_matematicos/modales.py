"""Modal de resultado reutilizable."""

import reflex as rx

from juegos_matematicos.style import button_play_style, link_style


def modal_resultado(
    state_cls: type,
    titulo_juego: str,
) -> rx.Component:
    """Diálogo con resultado, puntaje y acciones reintentar / menú."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(state_cls.texto_resultado),
            rx.dialog.description(
                rx.vstack(
                    rx.text(titulo_juego, weight="bold"),
                    rx.text(state_cls.mensaje),
                    rx.text(f"Puntaje: {state_cls.puntaje} / 100"),
                    rx.text(f"Tiempo restante: {state_cls.tiempo_restante} s"),
                    rx.text(f"Errores: {state_cls.errores}"),
                    spacing="2",
                    align="start",
                ),
            ),
            rx.hstack(
                rx.button(
                    "Reintentar",
                    on_click=state_cls.reintentar,
                    style=button_play_style,
                ),
                rx.button(
                    "Volver al menú",
                    on_click=state_cls.volver_menu,
                    style=link_style,
                ),
                spacing="4",
                margin_top="16px",
            ),
            max_width="420px",
        ),
        open=state_cls.modal_abierto,
    )
