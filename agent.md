# 🧠 agent.dm — Sistema de Juegos Matemáticos

## 1. 🎯 Propósito del Agente

El agente controla la lógica interna de los juegos matemáticos, asegurando:

* Coherencia matemática
* Generación de desafíos resolubles
* Evaluación de respuestas
* Gestión del tiempo y estados del juego

---

## 2. 🧩 Juegos Soportados

### 2.1 Juego de Álgebra con Frutas

#### Definición

Sistema de ecuaciones donde cada fruta representa una variable desconocida.

#### Objetivo del jugador

Determinar el valor numérico de cada fruta usando lógica.

---

### 2.2 Juego de Sucesiones

#### Definición

Reconocimiento de patrones numéricos (funciones ocultas).

#### Objetivo del jugador

Descubrir la regla y completar valores faltantes.

---

## 3. 🔁 Sistema de Estados (FSM)

```text
MENU → JUEGO_ACTIVO → RESULTADO → (REINTENTAR | MENU)
```

### Estados:

* MENU: selección de juego
* JUEGO_ACTIVO: interacción + temporizador
* RESULTADO: evaluación final + modal

---

## 4. 🍎 Lógica del Juego de Álgebra

### 4.1 Representación interna

```json
{
  "variables": {
    "🍎": null,
    "🍊": null,
    "🍌": null
  },
  "ecuaciones": [
    "🍎 + 🍎 = 4",
    "🍎 + 🍊 = 5",
    "🍊 + 🍌 = 7"
  ]
}
```

---

### 4.2 Reglas del sistema

1. Cada fruta representa UNA variable global

2. Las ecuaciones deben ser:

   * consistentes
   * resolubles
   * sin ambigüedad

3. Algunas frutas pueden:

   * no tener valor inicial
   * descubrirse indirectamente

---

### 4.3 Generación de niveles

#### Estrategia del agente:

1. Generar valores base:

```json
🍎 = 2
🍊 = 3
🍌 = 4
```

2. Construir ecuaciones derivadas:

```text
🍎 + 🍎 = 4
🍎 + 🍊 = 5
🍊 + 🍌 = 7
```

3. Ocultar valores

👉 IMPORTANTE:
El sistema NUNCA genera ecuaciones al azar.
Primero define la solución → luego construye el problema.

---

### 4.4 Evaluación

```pseudo
if respuesta_usuario == valores_reales:
    resultado = "correcto"
else:
    resultado = "incorrecto"
```

---

### 4.5 Tiempo

* Límite: 20 segundos
* Evento:

```pseudo
if tiempo == 0:
    finalizar_juego()
```

---

## 5. 🔢 Lógica del Juego de Sucesiones

### 5.1 Tipos de patrones

* Aritméticos (ej: +3, -2)
* Geométricos (ej: ×2)
* Fibonacci
* Primos
* Potencias
* Funciones mixtas

---

### 5.2 Representación

```json
{
  "secuencia": [2, 4, 8, null, null],
  "regla": "x2",
  "respuestas": [16, 32]
}
```

---

### 5.3 Reglas del agente

1. La secuencia debe tener:

   * UNA única regla clara
   * sin ambigüedad

2. Validación interna:

```pseudo
if multiples_reglas_posibles:
    descartar_secuencia()
```

---

### 5.4 Evaluación

```pseudo
correctas = contar_respuestas_correctas()

if correctas >= 3:
    resultado = "ganado"
else:
    resultado = "perdido"
```

---

### 5.5 Tiempo

* Límite: 30 segundos

---

## 6. 🧮 Sistema de Evaluación Global

```json
{
  "estado": "ganado | perdido",
  "puntaje": 0-100,
  "tiempo_restante": number,
  "errores": number
}
```

---

## 7. 🪟 Modal Final

### Contenido:

* Resultado (Correcto / Incorrecto)
* Puntaje
* Tiempo restante

### Acciones:

* 🔄 Reintentar
* 🏠 Volver al menú

---

## 8. ⚙️ Principios del Agente

1. **Primero solución, luego problema**
2. **Evitar ambigüedad**
3. **Escalar dificultad progresivamente**
4. **Tiempo como presión cognitiva**
5. **Feedback inmediato**

---

## 9. 🚀 Escalabilidad futura

* Niveles dinámicos
* IA generadora de problemas
* Ranking de jugadores
* Multijugador
* Adaptación por dificultad

---

## 10. 🧠 Analogía Ingenieril

Este sistema es equivalente a:

* Un **solver de ecuaciones**
* Un **generador de datasets controlados**
* Una **máquina de estados finitos**
* Un sistema de validación lógica

👉 Básicamente:
estás construyendo un mini motor matemático interactivo.
