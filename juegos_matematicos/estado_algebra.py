"""Estado Reflex del juego de ecuaciones con frutas."""

import asyncio

import reflex as rx

from juegos_matematicos.logica.algebra import (
    TIEMPO_LIMITE,
    evaluar_algebra,
    generar_nivel_algebra,
)


class AlgebraState(rx.State):
    fase: str = "activo"
    tiempo_restante: int = TIEMPO_LIMITE
    jugando: bool = False
    modal_abierto: bool = False

    frutas: list[str] = []
    ecuaciones: list[str] = []
    respuestas: list[str] = []
    valores_solucion: list[int] = []

    estado_resultado: str = ""
    puntaje: int = 0
    errores: int = 0
    mensaje: str = ""

    @rx.var
    def indices_frutas(self) -> list[int]:
        return list(range(len(self.frutas)))

    @rx.var
    def texto_resultado(self) -> str:
        if self.estado_resultado == "ganado":
            return "¡Correcto!"
        if self.tiempo_restante <= 0:
            return "Tiempo agotado"
        return "Incorrecto"

    @rx.event
    def iniciar(self):
        nivel = generar_nivel_algebra()
        self.frutas = nivel["frutas"]
        self.ecuaciones = nivel["ecuaciones"]
        self.valores_solucion = [nivel["solucion"][f] for f in self.frutas]
        self.respuestas = [""] * len(self.frutas)

        self.tiempo_restante = TIEMPO_LIMITE
        self.jugando = True
        self.fase = "activo"
        self.modal_abierto = False
        self.estado_resultado = ""
        self.puntaje = 0
        self.errores = 0
        self.mensaje = ""
        return AlgebraState.temporizador

    @rx.event(background=True)
    async def temporizador(self):
        while True:
            await asyncio.sleep(1)
            async with self:
                if not self.jugando:
                    return
                if self.tiempo_restante <= 0:
                    self._cerrar_partida(tiempo_agotado=True)
                    return
                self.tiempo_restante -= 1

    @rx.event
    def set_respuesta(self, valor: str, indice: int):
        if 0 <= indice < len(self.respuestas):
            nuevas = list(self.respuestas)
            nuevas[indice] = valor
            self.respuestas = nuevas

    @rx.event
    def comprobar(self):
        if not self.jugando:
            return
        self._cerrar_partida(tiempo_agotado=False)

    def _cerrar_partida(self, tiempo_agotado: bool):
        self.jugando = False
        self.fase = "resultado"
        solucion = {f: v for f, v in zip(self.frutas, self.valores_solucion)}
        if tiempo_agotado and not any(r.strip() for r in self.respuestas):
            res = {
                "estado": "perdido",
                "puntaje": 0,
                "tiempo_restante": 0,
                "errores": len(self.frutas),
            }
        else:
            res = evaluar_algebra(
                self.respuestas,
                self.frutas,
                solucion,
                self.tiempo_restante,
            )
        self.estado_resultado = res["estado"]
        self.puntaje = res["puntaje"]
        self.errores = res["errores"]
        self.tiempo_restante = res["tiempo_restante"]
        self.mensaje = (
            "Has acertado todas las frutas."
            if res["estado"] == "ganado"
            else f"Errores: {res['errores']}. Revisa las ecuaciones."
        )
        self.modal_abierto = True

    @rx.event
    def reintentar(self):
        self.modal_abierto = False
        return AlgebraState.iniciar

    @rx.event
    def volver_menu(self):
        self.modal_abierto = False
        self.jugando = False
        return rx.redirect("/")
