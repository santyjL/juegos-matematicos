import reflex as rx

config = rx.Config(
    app_name="juegos_matematicos",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)