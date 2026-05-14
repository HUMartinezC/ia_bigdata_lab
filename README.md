# IA + Big Data Lab

Laboratorio de análisis de datos enfocado en aplicaciones de **Inteligencia Artificial** y **Big Data** como parte de actividades educativas. El repositorio está compuesto principalmente por **notebooks** (Jupyter).

---

## 📋 Descripción

Este proyecto contiene prácticas y análisis de datos usando técnicas de *machine learning* (regresión, clasificación, árboles, etc.) y algunos ejercicios de visión por computador.  
Los notebooks están organizados por bloques temáticos para facilitar el seguimiento del temario.

---

## 📁 Estructura del proyecto

```
.
├── README.md                 # Este archivo
├── UTILS.md                  # Documentación de utilidades (utils/)
├── docker-compose.yml        # Entorno reproducible con Docker
├── docker/                   # Configuración/Dockerfile(s)
├── .env.example              # Plantilla de variables de entorno
├── data/                     # Datasets (local)
├── models/                   # Artefactos/modelos entrenados (joblib, etc.)
├── utils/                    # Funciones/clases auxiliares (ej: ModelManager)
└── notebooks/                # Notebooks organizados por tema
```

---

## 📗 Notebooks (qué contienen)

En general, los notebooks incluyen:

- **EDA / Análisis Exploratorio**
- **Limpieza y preprocesamiento**
- **Entrenamiento y evaluación de modelos**
- **Pipelines reproducibles**
- **Visualización y comunicación de resultados**
- **Experimentación con hiperparámetros y enfoques**

> Consejo: ejecuta los notebooks desde el entorno Docker para asegurar consistencia de dependencias.

---

## 🧰 Utilidades (utils/)

Este repo incluye utilidades para mejorar la reproducibilidad y la organización, por ejemplo:

- **ModelManager**: guardar/cargar modelos en `models/` siguiendo la estructura del notebook, evitando sobreescrituras accidentales.

Ver documentación completa en: **`UTILS.md`**.

---

## 🔧 Requisitos

### Opción A (Recomendado): Docker + Docker Compose
- Docker
- Docker Compose

### Opción B: Entorno local
- Python **3.8+**
- (Opcional) entorno virtual `venv`
- Paquetes según notebooks (pandas, scikit-learn, matplotlib, seaborn, etc.)

> Si no existe `requirements.txt`, la instalación de dependencias se hace “según el notebook” o según el entorno Docker.

---

## 🐳 Entorno reproducible con Docker (recomendado)

### 1) Configurar variables de entorno

Crear tu `.env` a partir del ejemplo:

```bash
cp .env.example .env
```

Variables típicas (según `.env.example`):
- `JUPYTER_ENABLE_LAB`
- `JUPYTER_PASSWORD`
- `JUPYTER_TOKEN` (si está vacío, puede autogenerarse)

### 2) Levantar el entorno

```bash
docker-compose up
```

Cuando el servicio esté arriba, Jupyter debería quedar accesible en:

- `http://localhost:8888/?token=TU_TOKEN_AQUI`

> El token debe coincidir con el configurado en tu `.env` (si aplica).

### 3) Ver logs (si algo falla)

```bash
docker-compose logs -f
```

---

## 🖥️ Usar Visual Studio Code con Jupyter remoto (opcional)

1. Instala extensiones:
   - Python (Microsoft)
   - Jupyter (Microsoft)
   - Pylance

2. Configura `.vscode/settings.json` para apuntar al servidor remoto:

```json
{
  "jupyter.jupyterServerType": "remote",
  "jupyter.remote.jupyterServerURI": "http://localhost:8888/?token=TU_TOKEN_AQUI",
  "jupyter.jupyterServerReuseType": "reuse"
}
```

---

## 🧪 Ejecución en local (sin Docker)

1. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
- Si el repo incorpora `requirements.txt`, usarlo:
  ```bash
  pip install -r requirements.txt
  ```
- Si no, instala según el notebook que vayas a ejecutar.

3. Ejecutar Jupyter:

```bash
jupyter lab
```

---

## 📚 Temas cubiertos

- ✅ **Manipulación de Datos**
- ✅ **Aprendizaje Supervisado – Regresiones**
  - Regresión lineal / múltiple
  - Regresión polinómica
  - Casos: coches, viviendas
- ✅ **Aprendizaje Supervisado – Clasificación**
  - Binaria (rendimiento estudiantil)
  - Multiclase (CIFAR-10)
  - Algoritmos: logística, SGD, baselines (dummy)
- ✅ **Árboles de decisión y bosques aleatorios**
- ✅ **Evaluación de modelos**
- ✅ **EDA y visualización**

---

## ✍️ Autor

HMartinez

---

**Última actualización:** Marzo 2026