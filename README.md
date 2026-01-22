# IA + Big Data Lab

Laboratorio de análisis de datos enfocado en aplicaciones de **Inteligencia Artificial** y **Big Data** como parte de actividades educativas.

## 📋 Descripción

Este proyecto contiene experimentos y análisis de datos utilizando técnicas de machine learning, incluyendo clasificación binaria y modelos de visión computacional. Los notebooks están organizados por tema de aprendizaje supervisado.

## 📁 Estructura del Proyecto

```
.
├── README.md                           # Este archivo
├── docker-compose.yml                  # Configuración de servicios Docker
├── docker/                             # Dockerfiles y configuración de contenedores
├── data/                               # Datos del proyecto (datasets)
├── models/                             # Modelos entrenados y artefactos
└── notebooks/
    └── 5_Aprendizaje_Supervisado/
        ├── 2_clasificacion_binaria_rendimiento_estudiantil.ipynb
        └── 3_clasificacion_cifar10.ipynb
```

## � Notebooks

Los notebooks contienen el trabajo práctico del laboratorio, incluyendo:

- **Análisis Exploratorio de Datos (EDA):** Investigación y visualización de datasets para entender patrones, distribuciones y relaciones entre variables
- **Preprocesamiento y Limpieza:** Tratamiento de datos faltantes, normalización, transformaciones y feature engineering
- **Entrenamiento de Modelos:** Implementación y ajuste de algoritmos de machine learning supervisado
- **Evaluación y Validación:** Métricas de rendimiento, validación cruzada, confusion matrices y comparación de modelos
- **Pipelines:** Construcción de flujos de trabajo reproducibles que integran múltiples etapas del análisis
- **Visualizaciones:** Gráficos y representaciones visuales para interpretar resultados y comunicar hallazgos
- **Experimentación:** Pruebas de diferentes enfoques, hiperparámetros y arquitecturas de modelos

Cada notebook es un documento ejecutable que combina código, resultados y explicaciones, permitiendo reproducir y entender el proceso completo de análisis y modelado.

## 🔧 Requisitos

- Python 3.8+
- Jupyter Notebook o JupyterLab
- Dependencias especificadas en el proyecto

## 🐳 Docker

El proyecto incluye configuración Docker para facilitar el entorno de desarrollo:

```bash
docker-compose up
```

## 📦 Uso

1. **Clonar o descargar el proyecto**
2. **Navegar a la carpeta del proyecto**
3. **Ejecutar los notebooks** desde Jupyter
4. **Consultar resultados** en la carpeta `models/` si hay artefactos guardados

## 📝 Variables de Entorno

Consultar `.env.example` para la configuración necesaria:

```bash
cp .env.example .env
# Editar .env con los valores apropiados
```

## 📚 Temas Cubiertos

- ✅ Aprendizaje Supervisado
- ✅ Clasificación Binaria
- ✅ Clasificación Multiclase (Visión Computacional)
- ✅ Análisis de rendimiento de modelos

## 🎯 Objetivos de Aprendizaje

Este laboratorio busca:
- Aplicar técnicas de machine learning a problemas reales
- Entender el pipeline completo de análisis de datos
- Evaluar y optimizar modelos predictivos
- Trabajar con diferentes tipos de datos (tabulares e imágenes)

## 📄 Notas

- Los datos se encuentran en la carpeta `data/`
- Los modelos entrenados se guardan en `models/`
- Cada notebook es independiente y puede ejecutarse por separado

*Crear `models/` de ser necesario.

## ✍️ Autor

HMartinez

Proyecto de aprendizaje - IA + Big Data

---

**Última actualización:** Enero 2026
