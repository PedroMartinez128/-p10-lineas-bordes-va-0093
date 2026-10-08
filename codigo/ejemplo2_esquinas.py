
import cv2
import numpy as np
# =================
#Pedro Martinez 0093
# =================

# Cargar imagen
imagen = cv2.imread("Lechuza-0093.jpg")

# Verificar que la imagen exista
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a tipo float32
gris_float = np.float32(gris)

# Detectar esquinas mediante Harris
esquinas = cv2.cornerHarris(
    gris_float,
    2,
    3,
    0.04
)

# Dilatar para hacer visibles las esquinas
esquinas = cv2.dilate(
    esquinas,
    None
)

# Crear copia
resultado = imagen.copy()

# Umbral para identificar esquinas
umbral = 0.05 * esquinas.max()

# Marcar esquinas
resultado[esquinas > umbral] = [0, 0, 255]

# Mostrar resultados
cv2.imshow(
    "Imagen original Lechuza 0093",
    imagen
)

cv2.imshow(
    "Esquinas detectadas Lechuza 0093",
    resultado
)

# Guardar resultado
cv2.imwrite(
    "C:\IA_Gpo3-H\VA_0093\p10-lineas-borde--va-0093\resultados.jpg",
    resultado
)

# Contar esquinas aproximadas
cantidad_esquinas = np.sum(
    esquinas > umbral
)

print("Deteccion de esquinas terminada.")
print("Cantidad aproximada de puntos detectados:",
      cantidad_esquinas)

print("Resultado guardado en:")
print("C:\IA_Gpo3-H\VA_0093\p10-lineas-borde--va-0093\resultados.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
#Pedro Martinez 0093
print("Pedro Martinez 0093")