# videoteca-python
Programa en Python que cuenta los títulos de una videoteca digital que cumplen una calificación mínima y un año límite. Fase 5 - Fundamentos de Programación (UNAD).

# Videoteca digital - Fase 5 Evaluación Final POA

Solución del **Problema 4** del curso Fundamentos de Programación (213022), UNAD.

## Descripción
Programa en Python que recibe un catálogo de películas guardado en una matriz con el formato `[Título, Año de lanzamiento, Calificación (1 a 10), Género]` y cuenta cuántos títulos cumplen **a la vez** dos criterios:

- Calificación mayor o igual a un umbral definido.
- Año de lanzamiento mayor o igual a un año límite.

## Cómo ejecutarlo
1. Tener Python 3 instalado.
2. Descargar el archivo `videoteca.py`.
3. Ejecutar en la terminal: `python videoteca.py`
4. Ingresar la calificación mínima y el año mínimo cuando el programa los pida.

## Ejemplo
Con calificación mínima `7.0` y año mínimo `2015`, el programa muestra:

```
Títulos que cumplen ambos criterios: 2
```

## Estructura de la solución
- `contar_titulos(catalogo, umbral, anio_limite)`: recorre la matriz con un ciclo `for` y cuenta los títulos que cumplen ambos criterios.
- Programa principal: define la matriz de 8 títulos, pide los criterios por teclado y muestra el total.

## Autor
Jose Sebastian Ramirez Ramirez - Ingeniería Multimedia, UNAD
