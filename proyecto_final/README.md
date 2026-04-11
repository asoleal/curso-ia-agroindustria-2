# Proyecto final

En esta carpeta se encuentra toda la información necesaria para desarrollar el proyecto final del curso de **Inteligencia Artificial para Agroindustria**.

Este `README.md` es el punto de entrada principal. Aquí se describe la ruta de trabajo, el objetivo del proyecto, los documentos que se deben leer y los datasets oficiales que se utilizarán.

---

## Objetivo del proyecto

El proyecto final tiene como objetivo que el estudiante desarrolle un ejercicio aplicado de inteligencia artificial, a partir de uno de los datasets oficiales del curso, integrando:

- comprensión del problema,
- explicación matemática básica del método,
- explicación conceptual del funcionamiento,
- ejemplo o ejercicio de apoyo,
- implementación del modelo en **PyTorch** o **TensorFlow**,
- documentación técnica en **LaTeX**,
- compilación final del informe en **PDF**.

No se busca únicamente entrenar un modelo, sino desarrollar un trabajo técnico, comprensible, reproducible y bien documentado.

---

## Ruta de trabajo

El estudiante debe seguir esta ruta dentro de la carpeta `proyecto_final/`:

### 1. Leer el enunciado general
Entrar a:

```text
proyecto_final/guia/enunciado_proyecto_final.md
```

En este archivo se encuentra la descripción general del proyecto, las modalidades disponibles, el enfoque del trabajo y los requisitos mínimos.

### 2. Leer la guía de entrega
Entrar a:

```text
proyecto_final/guia/entrega.md
```

En este archivo se explica cómo se debe realizar la entrega, qué debe contener el repositorio del estudiante en GitHub y qué archivos mínimos deben presentarse.

### 3. Revisar la rúbrica
Entrar a:

```text
proyecto_final/guia/rubrica.md
```

En este archivo se encuentran los criterios de evaluación del proyecto final.

### 4. Revisar los datasets oficiales
Entrar a:

```text
proyecto_final/datasets/
```

En esta carpeta se describe la información de los datasets oficiales del curso, tanto para la modalidad tabular como para la modalidad de imágenes.

### 5. Revisar los materiales de apoyo
Entrar a:

```text
proyecto_final/asignacion/
```

En esta carpeta se ubicarán notas técnicas, archivos base y otros materiales de apoyo para el desarrollo del proyecto.

---

## Qué se busca en el proyecto

Se espera que el estudiante:

1. Comprenda el problema asignado.
2. Trabaje con uno de los datasets oficiales del curso.
3. Explique de forma breve la base matemática del método usado.
4. Explique conceptualmente cómo funciona el modelo.
5. Presente un ejemplo, ejercicio o ilustración de apoyo.
6. Desarrolle un programa funcional en **PyTorch** o **TensorFlow**.
7. Documente todo el trabajo en **LaTeX**.
8. Compile el documento final en **PDF**.
9. Suba su trabajo al **GitHub del estudiante**.

---

## Modalidades del proyecto

Cada estudiante deberá escoger una de las siguientes modalidades:

### Modalidad 1. Clasificación tabular
Consiste en trabajar con un dataset tabular oficial del curso y desarrollar un modelo de clasificación.

### Modalidad 2. Clasificación de imágenes
Consiste en trabajar con un subconjunto oficial del dataset PlantVillage, usando imágenes de hojas de papa para clasificación.

---

## Datasets oficiales

Los datasets oficiales del curso están descritos en:

```text
proyecto_final/datasets/datasets_oficiales.md
```

### Dataset tabular
Ubicación de referencia:

```text
proyecto_final/datasets/tabular/
```

Incluye:

- un archivo `README.md`,
- un archivo `ejemplo_tabular.csv` para ilustrar el formato de los datos.

### Dataset de imágenes
Ubicación de referencia:

```text
proyecto_final/datasets/imagenes/
```

Incluye:

- un archivo `README.md`,
- un archivo `potato_subset.md` con la descripción del subconjunto seleccionado.

---

## Entrega

La entrega final debe realizarse en el **repositorio personal de GitHub del estudiante**.

Ese repositorio debe contener como mínimo:

- código fuente,
- documento en LaTeX,
- PDF compilado,
- `README.md`,
- resultados,
- instrucciones de ejecución.

---

## Estructura de esta carpeta

```text
proyecto_final/
├── README.md
├── guia/
│   ├── enunciado_proyecto_final.md
│   ├── entrega.md
│   └── rubrica.md
├── datasets/
│   ├── README.md
│   ├── datasets_oficiales.md
│   ├── tabular/
│   │   ├── README.md
│   │   └── ejemplo_tabular.csv
│   └── imagenes/
│       ├── README.md
│       └── potato_subset.md
└── asignacion/
    ├── README.md
    └── notas_tecnicas.md
```

---

## Recomendación final

Antes de comenzar a programar, el estudiante debe leer completamente los archivos de la carpeta `guia/` y revisar la modalidad de dataset que haya escogido.

