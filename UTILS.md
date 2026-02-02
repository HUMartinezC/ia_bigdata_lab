# 🛠️ Utilidades del Proyecto

Documentación de funciones y clases auxiliares disponibles en la carpeta `utils/`.

## 📦 ModelManager

Clase para gestionar el almacenamiento y carga de modelos de machine learning de forma organizada y consistente.

### Descripción

`ModelManager` proporciona una interfaz simplificada para:
- **Guardar modelos** con una estructura de carpetas coherente
- **Cargar modelos** guardados previamente
- **Evitar sobrescrituras accidentales** mediante parámetro obligatorio `overwrite`
- **Organización automática** por subcarpeta de notebook

### Estructura de almacenamiento

Los modelos se organizan en la siguiente estructura dentro de `models/`:

```
models/
├── 4_aprendizaje_supervisado_regresiones/
│   ├── 1_prediccion_precio_coches/
│   │   ├── modelo_lineal.joblib
│   │   └── modelo_polinomico.joblib
│   ├── 2_regresion_polinomica/
│   └── 3_prediccion_precios_viviendas/
├── 5_problemas_clasificacion/
│   ├── 2_clasificacion_binaria_rendimiento_estudiantil/
│   │   ├── logistic_regression.joblib
│   │   └── sgd_classifier.joblib
│   └── 3_clasificacion_cifar10/
│       ├── dummy_classifier_binary.joblib
│       ├── dummy_classifier_multiclass.joblib
│       └── sgd_classifier_multiclass.joblib
└── 6_arboles_decision_bosques_aleatorios/
    └── ...
```

**Patrón:** `/models/<notebook_subcarpeta>/<model_name>.joblib`

### Uso

#### 1. Importar ModelManager

```python
from utils.model_manager import ModelManager
```

#### 2. Instanciar ModelManager

Especificar la ruta relativa desde `notebooks/` al notebook actual:

```python
# Ejemplo para un notebook en: 
# notebooks/5_problemas_clasificacion/3_clasificacion_cifar10/

manager = ModelManager("5_problemas_clasificacion/3_clasificacion_cifar10")
```

#### 3. Guardar un modelo

```python
from sklearn.linear_model import LogisticRegression

# Entrenar modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Guardar (primero)
manager.save_model(modelo, "logistic_regression", overwrite=False)

# Actualizar (si existe)
modelo.fit(X_train_mejorado, y_train_mejorado)
manager.save_model(modelo, "logistic_regression", overwrite=True)
```

#### 4. Cargar un modelo

```python
# Cargar modelo guardado
modelo_cargado = manager.load_model("logistic_regression")

# Usar para predicción
predicciones = modelo_cargado.predict(X_test)
```

### Parámetros

#### Constructor

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `notebook_subpath` | `str` | **Obligatorio.** Ruta relativa desde `notebooks/` al notebook actual. Ejemplo: `"5_problemas_clasificacion/3_clasificacion_cifar10"` |

#### save_model()

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `model` | `object` | **Obligatorio.** Modelo a guardar (compatible con joblib) |
| `model_name` | `str` | **Obligatorio.** Nombre descriptivo sin extensión. Ejemplo: `"random_forest"` |
| `overwrite` | `bool` | **Obligatorio.** Debe ser `True` o `False` explícitamente. Si `False` y el archivo existe, lanza `FileExistsError` |

#### load_model()

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `model_name` | `str` | **Obligatorio.** Nombre del modelo guardado (sin extensión) |

### Ejemplos completos

#### Ejemplo 1: Clasificación Binaria

```python
from utils.model_manager import ModelManager
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Instanciar manager
manager = ModelManager("5_problemas_clasificacion/2_clasificacion_binaria_rendimiento_estudiantil")

# Cargar datos
df = pd.read_csv("../../../data/car_evaluation.csv")

# Preparar datos
X = df.drop("target", axis=1)
y = df["target"]

# Modelo 1: Regresión Logística
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X, y)
manager.save_model(lr_model, "logistic_regression", overwrite=False)

# Modelo 2: Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)
manager.save_model(rf_model, "random_forest", overwrite=False)

# Cargar y evaluar
modelo_cargado = manager.load_model("random_forest")
accuracy = modelo_cargado.score(X, y)
print(f"Accuracy: {accuracy:.4f}")
```

#### Ejemplo 2: SGDClassifier con CIFAR-10

```python
from utils.model_manager import ModelManager
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

manager = ModelManager("5_problemas_clasificacion/3_clasificacion_cifar10")

# Crear pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('sgd', SGDClassifier(loss='hinge', n_jobs=-1, random_state=42))
])

# Entrenar (primera ejecución: ~5 minutos)
pipe.fit(X_train_flattened, y_train)
manager.save_model(pipe, "sgd_classifier_multiclass", overwrite=False)

# Ejecuciones posteriores: cargar directamente (< 1 segundo)
pipe_cargado = manager.load_model("sgd_classifier_multiclass")
predicciones = pipe_cargado.predict(X_test_flattened)
accuracy = pipe_cargado.score(X_test_flattened, y_test)
print(f"Accuracy: {accuracy:.4f}")
```

#### Ejemplo 3: Regresión Polinómica

```python
from utils.model_manager import ModelManager
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

manager = ModelManager("4_aprendizaje_supervisado_regresiones/2_regresion_polinomica")

# Crear pipeline
pipe = Pipeline([
    ('poly_features', PolynomialFeatures(degree=3)),
    ('linear_regression', LinearRegression())
])

# Entrenar
pipe.fit(X_train, y_train)

# Guardar
manager.save_model(pipe, "pipeline_polinomio_grado3", overwrite=False)

# Cargar más tarde
pipe_cargado = manager.load_model("pipeline_polinomio_grado3")
predicciones = pipe_cargado.predict(X_test)
```

### Manejo de errores

#### ValueError: notebook_subpath no especificado

```python
# ❌ INCORRECTO
manager = ModelManager("")  # ValueError

# ✅ CORRECTO
manager = ModelManager("5_problemas_clasificacion/3_clasificacion_cifar10")
```

#### FileExistsError: Modelo ya existe

```python
# Primera ejecución
manager.save_model(model, "mi_modelo", overwrite=False)  # ✅ Funciona

# Segunda ejecución sin cambios
manager.save_model(model, "mi_modelo", overwrite=False)  # ❌ FileExistsError

# Para actualizar
manager.save_model(model, "mi_modelo", overwrite=True)   # ✅ Funciona
```

#### FileNotFoundError: Modelo no encontrado

```python
manager.load_model("modelo_inexistente")  # FileNotFoundError
```

### Características técnicas

- **Formato:** Utiliza `joblib` para serialización (compatible con scikit-learn)
- **Rutas:** Funciona en entorno Docker (`/home/jovyan/work/`) y sistemas locales
- **Validación:** Valida parámetros obligatorios y evita errores comunes
- **Logs:** Imprime ruta completa al guardar/cargar para trazabilidad
- **Creación de carpetas:** Las crea automáticamente si no existen

### Casos de uso recomendados

`ModelManager` es especialmente útil cuando:

- **Entrenamientos largos:** Modelos que tardan minutos/horas (ej: SGDClassifier con CIFAR-10)
- **Múltiples re-ejecuciones:** Debugging, ajuste de visualizaciones o métricas
- **Comparación de modelos:** Varios modelos entrenados en el mismo notebook
- **Reproducibilidad:** Garantizar que el mismo modelo se carga en diferentes sesiones
- **Colaboración:** Compañeros pueden cargar tu modelo sin reentrenarlo

### Modelos existentes

Ver carpeta [models/](models/) para consultar modelos ya entrenados en el proyecto:

```bash
find models/ -name "*.joblib" | sort
```

---

*Última actualización: Febrero 2026*
