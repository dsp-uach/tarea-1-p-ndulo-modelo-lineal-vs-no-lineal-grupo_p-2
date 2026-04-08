# ACUS125 — Tarea 1: Péndulo simple (modelo lineal vs no lineal)

---

## Objetivo

En esta actividad explorarás el comportamiento dinámico de un péndulo simple comparando:

- el modelo **no lineal real**
- el modelo **lineal aproximado**

A través de simulaciones en Python, podrás:

- visualizar el movimiento en el tiempo  
- analizar diferencias entre modelos  
- estudiar cómo cambia el período con la amplitud  
- comprender cuándo la aproximación lineal es válida  

---

## Modelos

### Modelo no lineal

$\ddot{\theta} + \frac{g}{L}\sin(\theta) = 0$

---

### Modelo lineal (aproximación por serie de Taylor)

$\sin(\theta) \approx \theta$

Entonces:

$\ddot{\theta} + \frac{g}{L}\theta = 0$

---

## Pregunta central

> ¿Para qué ángulos iniciales el modelo lineal representa correctamente el movimiento del péndulo?

---

## Instrucciones

```bash
python scripts/02_explore_pendulum_models.py
```

---

## Actividades

### Parte 1 — Observación

- Ejecuta el script  
- Observa diferencias entre modelos  

---

### Parte 2 — Análisis

1. ¿Cómo cambia el error al aumentar el ángulo?  
2. ¿El error crece en el tiempo?  
3. ¿Qué ocurre con el período?  

---

### Parte 3 — Interpretación

4. Explica el desfase entre modelos  
5. ¿Qué significa que la frecuencia dependa de la amplitud?  

---

### Parte 4 — Exploración

- prueba nuevos ángulos  
- modifica tiempo de simulación  

---

## Aplicaciones reales

### Relojes de péndulo
Errores en tiempo si amplitud aumenta.

### Estructuras
No linealidad en terremotos y grandes desplazamientos.

### Mecánica y robótica
Grandes ángulos → modelo lineal falla.

### Acústica
Grandes amplitudes → distorsión.

---

## Reflexión del grupo de trabajo

> ¿Qué consecuencias prácticas tendría usar el modelo lineal en un sistema real cuando no es válido?

---

## Exploración adicional

Investiga otro sistema no lineal.

---

## Exploración opcional — efecto del largo

Modifica el parámetro del sistema:

```python
L = 0.5
L = 1.0
L = 2.0
```

Responde:

1. ¿Cómo cambia el período del sistema?  
2. ¿El error entre modelos cambia en magnitud o en escala temporal?  
3. ¿El largo afecta la validez de la aproximación lineal?  

Pista: el largo controla la escala temporal del sistema, pero no la no linealidad.

---

## Entregable

- respuestas  
- gráficos  
- reflexión  

---

## Rúbrica

| Criterio | Puntaje |
|----------|--------|
| Comprensión | 2 |
| Análisis | 2 |
| Período | 2 |
| Exploración | 2 |
| Reflexión | 2 |

Total: 10

---

## Mensaje final

Un modelo simple es útil… pero tiene límites.
