import joblib
import os
import inspect


class ModelManager:
    """
    Clase para gestionar el guardado y carga de modelos de machine learning.
    Estructura de directorios:
    models/
        ├── <carpeta_padre_notebook>/
            ├── <carpeta_nombre_notebook>/
                ├── <nombre_modelo>.joblib
    """

    def __init__(self, base_dir=None):
        try:
            # Obtener ruta raíz del proyecto
            current_file = inspect.getfile(inspect.currentframe())
            project_root = os.path.abspath(
                os.path.join(os.path.dirname(current_file), "..", "..")
            )

            # Definir directorio base para guardar modelos
            if base_dir is None:
                base_dir = os.path.join(project_root, "models")

            self.base_dir = base_dir

            # Crear el directorio base si no existe
            if not os.path.exists(self.base_dir):
                os.makedirs(self.base_dir)
        except Exception as e:
            raise RuntimeError("No se pudo inicializar el ModelManager.") from e

    def _get_notebook_info(self):
        """
        Obtiene el nombre del notebook y su carpeta padre.
        """
        frame = inspect.currentframe()
        try:
            # Retroceder frames: _get_notebook_info -> _get_model_dir -> save/load_model -> usuario
            caller_frame = (
                frame.f_back.f_back
                if frame.f_back and frame.f_back.f_back
                else frame.f_back
            )
            if not caller_frame:
                raise RuntimeError("No se puede obtener el frame del llamador.")

            file = inspect.getfile(caller_frame)
            notebook_path = os.path.abspath(file)

            parent_folder = os.path.basename(os.path.dirname(notebook_path))
            notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]

            return parent_folder, notebook_name

        except Exception as e:
            raise RuntimeError(
                "No se pudo obtener la información del notebook. "
                "Asegúrate de ejecutar esto dentro de un Jupyter Notebook."
            ) from e
        finally:
            del frame

    def _get_model_dir(self):
        """
        Obtiene el directorio donde se guardarán los modelos para el notebook actual.
        """
        try:
            parent_folder, notebook_name = self._get_notebook_info()
            model_dir = os.path.join(self.base_dir, parent_folder, notebook_name)
            os.makedirs(model_dir, exist_ok=True)
            return model_dir
        except Exception as e:
            raise RuntimeError(
                "No se pudo obtener o crear el directorio del modelo."
            ) from e

    def save_model(self, model, model_name, overwrite=False):
        """
        Guarda el modelo en el directorio correspondiente utilizando joblib.
        :param model: Modelo a guardar.
        :param model_name: Nombre del modelo (sin extensión).
        :param overwrite (bool): Indica si se debe sobrescribir un modelo existente (default: False).
        """

        try:
            if not model_name:
                raise ValueError("El parámetro 'model_name' es obligatorio.")

            if model is None:
                raise ValueError("El parámetro 'model' es obligatorio.")

            if overwrite not in [True, False]:
                raise ValueError(
                    "Debes especificar explícitamente overwrite=True o overwrite=False"
                )

            model_dir = self._get_model_dir()
            model_path = os.path.join(model_dir, f"{model_name}.joblib")

            if not overwrite and os.path.exists(model_path):
                raise FileExistsError(
                    f"El modelo '{model_name}' ya existe en {model_dir}. "
                    f"Usa overwrite=True para sobrescribir."
                )

            joblib.dump(model, model_path)
            print(f"Modelo guardado en: {model_path}")
        except (ValueError, FileExistsError):
            raise
        except Exception as e:
            raise RuntimeError("Error al guardar el modelo.") from e

    def load_model(self, model_name):
        """
        Carga un modelo guardado previamente.
        """
        try:
            if not model_name:
                raise ValueError("El parámetro 'model_name' es obligatorio.")

            model_dir = self._get_model_dir()
            model_path = os.path.join(model_dir, f"{model_name}.joblib")
            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"No se encontró el modelo '{model_name}' en {model_dir}"
                )
            model = joblib.load(model_path)
            print(f"Modelo cargado desde: {model_path}")
            return model
        except (ValueError, FileNotFoundError):
            raise
        except Exception as e:
            raise RuntimeError("Error al cargar el modelo.") from e
