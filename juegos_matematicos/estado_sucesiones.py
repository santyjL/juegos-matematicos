"""Estado Reflex del juego de sucesiones."""

import asyncio

import reflex as rx

from juegos_matematicos.logica.sucesiones import (
    TIEMPO_LIMITE,
    evaluar_sucesion,
    generar_nivel_sucesion,
)


class SucesionesState(rx.State):
    fase: str = "activo"
    tiempo_restante: int = TIEMPO_LIMITE
    jugando: bool = False
    modal_abierto: bool = False

    secuencia: list[int] = []
    es_oculto: list[bool] = []
    respuestas: list[str] = []
    regla: str = ""
    respuestas_esperadas: list[int] = []

    estado_resultado: str = ""
    puntaje: int = 0
    errores: int = 0
    mensaje: str = ""

    @rx.var
    def indices_secuencia(self) -> list[int]:
        return list(range(len(self.secuencia)))

    @rx.var
    def indices_respuestas(self) -> list[int]:
        return list(range(len(self.respuestas)))

    @rx.var
    def texto_resultado(self) -> str:
        if self.estado_resultado == "ganado":
            return "¡Patrón encontrado!"
        return "Sigue practicando"

    @rx.event
    def iniciar(self):
        nivel = generar_nivel_sucesion()
        self.secuencia = [
            x if x is not None else 0 for x in nivel["secuencia"]
        ]
        self.es_oculto = [x is None for x in nivel["secuencia"]]
        self.respuestas_esperadas = nivel["respuestas_esperadas"]
        self.respuestas = [""] * len(self.respuestas_esperadas)
        self.regla = nivel["regla"]

        self.tiempo_restante = TIEMPO_LIMITE
        self.jugando = True
        self.fase = "activo"
        self.modal_abierto = False
        self.estado_resultado = ""
        self.puntaje = 0
        self.errores = 0
        self.mensaje = ""
        return SucesionesState.temporizador

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
        if tiempo_agotado and not any(r.strip() for r in self.respuestas):
            res = {
                "estado": "perdido",
                "puntaje": 0,
                "tiempo_restante": 0,
                "errores": len(self.respuestas_esperadas),
            }
        else:
            res = evaluar_sucesion(
                self.respuestas,
                self.respuestas_esperadas,
                self.tiempo_restante,
            )
        self.estado_resultado = res["estado"]
        self.puntaje = res["puntaje"]
        self.errores = res["errores"]
        self.tiempo_restante = res["tiempo_restante"]
        self.mensaje = (
            "Al menos 3 respuestas correctas. ¡Bien!"
            if res["estado"] == "ganado"
            else f"Necesitas 3 aciertos. Errores: {res['errores']}."
        )
        self.modal_abierto = True

    @rx.event
    def reintentar(self):
        self.modal_abierto = False
        return SucesionesState.iniciar

    @rx.event
    def volver_menu(self):
        self.modal_abierto = False
        self.jugando = False
        return rx.redirect("/")
