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
├── .vscode/                            # Configuración de Visual Studio Code
│   └── settings.json                   # Configuración de JupyterLab remoto
├── .env.example                        # Variables de entorno (template)
├── data/                               # Datos del proyecto (datasets)
├── models/                             # Modelos entrenados y artefactos
├── utils/                              # Utilidades y funciones auxiliares
└── notebooks/                          # Notebooks organizados por tema
    ├── 2_proyectos_ml/
    │   └── 2_1_manipulacion_datos.ipynb
    ├── 4_aprendizaje_supervisado_regresiones/
    │   ├── 1_prediccion_precio_coches.ipynb
    │   ├── 2_regresion_polinomica.ipynb
    │   └── 3_prediccion_precios_viviendas.ipynb
    ├── 5_problemas_clasificacion/
    │   ├── 2_clasificacion_binaria_rendimiento_estudiantil.ipynb
    │   └── 3_clasificacion_cifar10.ipynb
    ├── 6_arboles_decision_bosques_aleatorios/
    │   ├── 1_arboles_de_decision.ipynb
    │   ├── 2_nivel_seguridad_automoviles.ipynb
    │   └── 3_arboles_prediccion_cardiopatia.ipynb
    └── convertir_a_pdf.ipynb           # Utilidad para convertir notebooks a PDF
```

## 📗 Notebooks

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

- **Python 3.8+**
- **Docker y Docker Compose** (para entorno containerizado)
- **Jupyter Lab** (se ejecuta dentro del contenedor Docker)
- **Visual Studio Code** (opcional, pero recomendado para mejor integración)
- **Dependencias Python:** pandas, scikit-learn, matplotlib, seaborn, tensorflow/torch (según notebooks)

## 🐳 Docker reproducible:

### Levantar el entorno

```bash
docker-compose up
```

El servicio de Jupyter Lab estará disponible en `http://localhost:8888/?token=TU_TOKEN_AQUI` con el token configurado en `.env`bash
docker-compose up
### Opción 1: Con Docker (Recomendado)

1. **Clonar o descargar el proyecto**
2. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   # Editar .env con valores (JUPYTER_TOKEN, contraseña, etc.)
   ```
3. **Levantar el contenedor:**
   ⚙️ Configuración de Variables de Entorno

Crear archivo `.env` basado en `.env.example`:

```bash
cp .env.example .env
```

**Variables disponibles:**
- `JUPYTER_ENABLE_LAB`: Activar JupyterLab (true/false)
- `JUPYTER_PASSWORD`: Contraseña para acceder a Jupyter
- `JUPYTER_TOKEN`: Token de seguridad para Jupyter (se genera automáticamente si está vacío)

## 🖥️ Configuración de Visual Studio Code

Para optimizar la experiencia con Jupyter Lab desde VS Code:

1. **Instalar extensiones recomendadas:**
   - `Python` (Microsoft)
   - `Jupyter` (Microsoft)
   - `Pylance` (para autocompletado)

2. **Actualizar token en `.vscode/settings.json`:**
   ```json
   {
     "jupyter.jupyterServerType": "remote",
     "jupyter.remote.jupyterServerURI": "http://localhost:8888/?token=TU_TOKEN_AQUI",
     "jupyter.jupyterServerReuseType": "reuse"
   }
   ```
   - El `token` debe coincidir con `JUPYTER_TOKEN` en `.env`
   - Con `"reuse": true`, VS Code manteniene la conexión sin reconectar

3. **Ejecutar notebooks desde VS Code:**
   - Abrir `.ipynb` y VS Code conectará automáticamente a Jupyter remoto
   - Las celdas se ejecutarán en el kernel del contenedor Docker
1. **Levantar Docker primero** (seguir pasos 1-3 arriba)
2. **Abrir la carpeta del proyecto** en VS Code
3. **Conectar a Jupyter remoto:**
   - La configuración en `.vscode/settings.json` conectará automáticamente a JupyterLab
   - Si es la primera vez, actualizar el token en `.vscode/settings.json` con el token de tu `.env`
   - Ejecutar notebooks directamente desde el editor
   - VS Code reutilizará la conexión sin reconectar manualmente

### Opción 3: Entorno local (sin Docker)

1. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar Jupyter Lab:**
   ```bash
   jupyter lab
   ```
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

- ✅ **Manipulación de Datos:** Limpieza, transformación y preparación de datasets
- ✅ **Aprendizaje Supervisado - Regresiones:** Predicción de valores continuos
  - Regresión Lineal Simple y Múltiple
  - Regresión Polinómica
  - Predicción de precios (coches, viviendas)
- ✅ **Aprendizaje Supervisado - Clasificación:** Predicción de categorías
  - Clasificación Binaria (rendimiento estudiantil)
  - Clasificación Multiclase (CIFAR-10 con visión computacional)
  - Algoritmos: Logística, SGD, Clasificadores Dummy
- ✅ **Árboles de Decisión y Bosques Aleatorios:**
  - Construcción y interpretación de árboles
  - Random Forests para clasificación
  - Predicción de seguridad en automóviles
  - Predicción de cardiopatía
- ✅ **Evaluación de Modelos:** Métricas, validación cruzada, matriz de confusión
- ✅ **Análisis Exploratorio (EDA):** Visualizaciones y descubrimiento de patrones

## 🎯 Objetivos de Aprendizaje

E*Notas de implementación:**
- Crear carpeta `models/` si no existe para almacenar modelos entrenados
- Instalar `requirements.txt` si se usa entorno local
- Consultar logs del contenedor con `docker-compose logs jupyter` para debugging

## ✍️ Autor

HMartinez

Proyecto de aprendizaje - IA + Big Data

---

**Última actualización:** Febrero 2026
