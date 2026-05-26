"""API pública del motor matemático (agente)."""

from juegos_matematicos.logica.algebra import (
    TIEMPO_LIMITE as TIEMPO_ALGEBRA,
    NivelAlgebra,
    evaluar_algebra,
    generar_nivel_algebra,
)
from juegos_matematicos.logica.evaluacion import calcular_puntaje, resultado_global
from juegos_matematicos.logica.sucesiones import (
    TIEMPO_LIMITE as TIEMPO_SUCESIONES,
    MIN_CORRECTAS,
    NivelSucesion,
    evaluar_sucesion,
    generar_nivel_sucesion,
)

__all__ = [
    "TIEMPO_ALGEBRA",
    "TIEMPO_SUCESIONES",
    "MIN_CORRECTAS",
    "NivelAlgebra",
    "NivelSucesion",
    "calcular_puntaje",
    "resultado_global",
    "generar_nivel_algebra",
    "evaluar_algebra",
    "generar_nivel_sucesion",
    "evaluar_sucesion",
]
