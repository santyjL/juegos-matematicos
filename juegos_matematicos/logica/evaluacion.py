"""Utilidades compartidas de puntuación y resultado."""

from typing import Literal

EstadoResultado = Literal["ganado", "perdido"]


def calcular_puntaje(
    correctas: int,
    total: int,
    tiempo_restante: int,
    tiempo_limite: int,
) -> int:
    """Puntaje 0-100 según aciertos y tiempo restante."""
    if total <= 0:
        return 0
    base = int((correctas / total) * 80)
    bonus_tiempo = int((tiempo_restante / max(tiempo_limite, 1)) * 20)
    return min(100, base + bonus_tiempo)


def resultado_global(
    ganado: bool,
    puntaje: int,
    tiempo_restante: int,
    errores: int,
) -> dict:
    estado: EstadoResultado = "ganado" if ganado else "perdido"
    return {
        "estado": estado,
        "puntaje": puntaje,
        "tiempo_restante": tiempo_restante,
        "errores": errores,
    }
