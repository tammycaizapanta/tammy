#TALLER
"""Implementar un programa en Python que analiza frases simples y predice su categoría usando
un método basado en conteos de palabras. Puede contener os datos simples como por ejemplo:
"pantalla no carga", "bug"
"cómo cambiar contraseña", "consulta"
"error en login", "bug"
"dónde está el menú", "consulta"
Los estudiantes deben utilizar otro tipo de ejemplos, diferente al ya mencionado.
El código será corto y fácil de entender: no usará librerías complejas ni estructuras avanzadas.
Sólo se necesitarán listas, diccionarios y condicionales. Además, se explicarán conceptos paso a
paso y con ejemplos claros."""

# Datos de entrenamiento
datos_entrenamiento = [
    ("la aplicación se cierra sola", "bug"),
    ("no puedo iniciar sesión", "bug"),
    ("cómo puedo cambiar el idioma", "consulta"),
    ("qué funciones tiene la aplicación", "consulta"),
    ("se bloquea cuando presiono guardar", "bug"),
    ("dónde configuro las notificaciones", "consulta"),
    ("pantalla negra al abrir", "bug"),
    ("para qué sirve esta opción", "consulta")
]

# Paso 1: Conteo de palabras por categoría
conteo_categorias = {"bug": 0, "consulta": 0}
palabras_por_categoria = {"bug": {}, "consulta": {}}
total_palabras_por_categoria = {"bug": 0, "consulta": 0}

for mensaje, categoria in datos_entrenamiento:
    conteo_categorias[categoria] += 1
    palabras = mensaje.lower().split()
    for palabra in palabras:
        palabras_por_categoria[categoria][palabra] = palabras_por_categoria[categoria].get(palabra, 0) + 1
        total_palabras_por_categoria[categoria] += 1

# Paso 2: Función para clasificar y mostrar probabilidades
def clasificar_mensaje(mensaje):
    palabras = mensaje.lower().split()
    probabilidades = {}
    print(f"\n🔍 Clasificando mensaje: \"{mensaje}\"")

    for categoria in ["bug", "consulta"]:
        print(f"\n📂 Categoría: {categoria}")
        probabilidad = conteo_categorias[categoria] / sum(conteo_categorias.values())
        print(f"  P({categoria}) = {conteo_categorias[categoria]}/{sum(conteo_categorias.values())} = {probabilidad:.4f}")

        for palabra in palabras:
            conteo_palabra = palabras_por_categoria[categoria].get(palabra, 0)
            # Suavizado de Laplace
            total = total_palabras_por_categoria[categoria] + len(palabras_por_categoria[categoria])
            prob_palabra = (conteo_palabra + 1) / total
            probabilidad *= prob_palabra
            print(f"  P({palabra} | {categoria}) = ({conteo_palabra} + 1) / {total} = {prob_palabra:.4f}")

        probabilidades[categoria] = probabilidad
        print(f"  → Probabilidad total P({categoria} | mensaje) ≈ {probabilidad:.8f}")

    # Decisión final
    if probabilidades["bug"] > probabilidades["consulta"]:
        resultado = "bug"
    elif probabilidades["bug"] < probabilidades["consulta"]:
        resultado = "consulta"
    else:
        resultado = "empate"

    print(f"\n✅ Resultado: El mensaje se clasifica como → {resultado.upper()}")
    return resultado

# 🌟 Ejemplos de prueba
mensajes_prueba = [
    "la aplicación se traba al guardar",
    "cómo elimino una cuenta",
    "no responde el botón",
    "dónde veo mi historial"
]

for mensaje in mensajes_prueba: 
    clasificar_mensaje(mensaje)