# Aplicacion del Algebra matricial creando Un vocabulario unico y una matriz de terminos
import numpy as np

# Documentos de ejemplo
documentos = [
    "el gato está en la casa",
    "el perro está en el jardín",
    "la casa es grande"
]

# Crear un vocabulario único
vocabulario = set(" ".join(documentos).split())
vocabulario = sorted(vocabulario)  # Ordenar el vocabulario

# Crear la matriz de términos
matriz_terminos = np.zeros((len(documentos), len(vocabulario)))

# Llenar la matriz con las frecuencias de términos
for i, doc in enumerate(documentos):
    for palabra in doc.split():
        j = vocabulario.index(palabra)
        matriz_terminos[i, j] += 1

  print("Matriz de términos:\n", matriz_terminos)

# Calcular la similitud entre documentos
similitud = np.dot(matriz_terminos, matriz_terminos.T)

print("Matriz de similitud:\n", similitud)
