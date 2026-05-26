"""Generación y evaluación del juego de ecuaciones con frutas."""

import random
from typing import TypedDict

from juegos_matematicos.logica.evaluacion import calcular_puntaje, resultado_global

FRUTAS_POOL = ["🍎", "🍊", "🍌", "🍓", "🍇"]
TIEMPO_LIMITE = 20


class NivelAlgebra(TypedDict):
    frutas: list[str]
    ecuaciones: list[str]
    solucion: dict[str, int]


def _formatear_ecuacion(terminos: list[str], resultado: int) -> str:
    return " + ".join(terminos) + f" = {resultado}"


def generar_nivel_algebra(
    num_frutas: int = 3,
) -> NivelAlgebra:
    """Primero solución, luego ecuaciones derivadas (sin ambigüedad)."""
    frutas = random.sample(FRUTAS_POOL, num_frutas)
    solucion = {f: random.randint(1, 9) for f in frutas}

    ecuaciones: list[str] = []
    f0, f1, f2 = frutas[0], frutas[1], frutas[2] if len(frutas) > 2 else frutas[1]

    ecuaciones.append(
        _formatear_ecuacion([f0, f0], solucion[f0] * 2)
    )
    ecuaciones.append(
        _formatear_ecuacion([f0, f1], solucion[f0] + solucion[f1])
    )
    if len(frutas) >= 3:
        ecuaciones.append(
            _formatear_ecuacion([f1, f2], solucion[f1] + solucion[f2])
        )
        ecuaciones.append(
            _formatear_ecuacion([f0, f2], solucion[f0] + solucion[f2])
        )
    else:
        ecuaciones.append(
            _formatear_ecuacion([f1, f1], solucion[f1] * 2)
        )

    return {
        "frutas": frutas,
        "ecuaciones": ecuaciones,
        "solucion": solucion,
    }


def evaluar_algebra(
    respuestas: list[str],
    frutas: list[str],
    solucion: dict[str, int],
    tiempo_restante: int,
) -> dict:
    errores = 0
    correctas = 0
    total = len(frutas)

    for i, fruta in enumerate(frutas):
        esperado = solucion[fruta]
        try:
            valor = int(str(respuestas[i]).strip())
            if valor == esperado:
                correctas += 1
            else:
                errores += 1
        except (ValueError, IndexError):
            errores += 1

    ganado = errores == 0 and correctas == total
    puntaje = calcular_puntaje(
        correctas, total, tiempo_restante, TIEMPO_LIMITE
    )
    return resultado_global(ganado, puntaje, tiempo_restante, errores)
