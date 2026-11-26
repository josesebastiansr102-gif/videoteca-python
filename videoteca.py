def contar_titulos(catalogo, umbral, anio_limite):
    """Cuenta los títulos con calificación >= umbral Y año >= anio_limite."""
    contador = 0
    for titulo in catalogo:
        anio = titulo[1]
        calificacion = titulo[2]
        if calificacion >= umbral and anio >= anio_limite:
            contador += 1
    return contador


# Matriz: [Título, Año de lanzamiento, Calificación (1 a 10), Género]
catalogo = [
    ["Your Name", 2016, 8.4, "Animación"],
    ["El Conjuro", 2013, 7.5, "Terror"],
    ["Cars", 2006, 7.2, "Animación"],
    ["Haz que regrese", 2025, 6.9, "Terror"],
    ["La era de hielo 3", 2009, 6.7, "Animación"],
    ["Abigail", 2024, 6.6, "Terror"],
    ["Backrooms", 2026, 6.0, "Terror"],
    ["La sustancia", 2024, 7.3, "Terror"],
]

umbral = float(input("Calificación mínima (1 a 10): "))
anio_limite = int(input("Año de lanzamiento mínimo: "))

total = contar_titulos(catalogo, umbral, anio_limite)
print(f"Títulos que cumplen ambos criterios: {total}")
