"""Generación y evaluación del juego de sucesiones."""

import random
from typing import Literal, TypedDict

from juegos_matematicos.logica.evaluacion import calcular_puntaje, resultado_global

TIEMPO_LIMITE = 30
MIN_CORRECTAS = 3
LARGO_SECUENCIA = 7
OCULTOS = 3

TipoPatron = Literal["aritmetica", "geometrica"]


class NivelSucesion(TypedDict):
    secuencia: list[int | None]
    respuestas_esperadas: list[int]
    regla: str
    tipo: TipoPatron


def _generar_aritmetica() -> tuple[list[int], str]:
    inicio = random.randint(2, 12)
    diff = random.randint(2, 6)
    seq = [inicio + i * diff for i in range(LARGO_SECUENCIA)]
    regla = f"Suma {diff} cada vez (+{diff})"
    return seq, regla


def _generar_geometrica() -> tuple[list[int], str]:
    inicio = random.randint(2, 5)
    ratio = random.choice([2, 3])
    seq = [inicio * (ratio**i) for i in range(LARGO_SECUENCIA)]
    regla = f"Multiplica por {ratio} cada vez (×{ratio})"
    return seq, regla


def generar_nivel_sucesion() -> NivelSucesion:
    tipo: TipoPatron = random.choice(["aritmetica", "geometrica"])
    if tipo == "aritmetica":
        completa, regla = _generar_aritmetica()
    else:
        completa, regla = _generar_geometrica()

    visibles = completa[: LARGO_SECUENCIA - OCULTOS]
    ocultos_valores = completa[LARGO_SECUENCIA - OCULTOS :]
    secuencia: list[int | None] = visibles + [None] * OCULTOS

    return {
        "secuencia": secuencia,
        "respuestas_esperadas": ocultos_valores,
        "regla": regla,
        "tipo": tipo,
    }


def evaluar_sucesion(
    respuestas: list[str],
    esperadas: list[int],
    tiempo_restante: int,
) -> dict:
    correctas = 0
    errores = 0
    total = len(esperadas)

    for i, esperado in enumerate(esperadas):
        try:
            valor = int(str(respuestas[i]).strip())
            if valor == esperado:
                correctas += 1
            else:
                errores += 1
        except (ValueError, IndexError):
            errores += 1

    ganado = correctas >= MIN_CORRECTAS
    puntaje = calcular_puntaje(
        correctas, total, tiempo_restante, TIEMPO_LIMITE
    )
    return resultado_global(ganado, puntaje, tiempo_restante, errores)
