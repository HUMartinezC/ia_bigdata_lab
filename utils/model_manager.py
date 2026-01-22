from pathlib import Path
import joblib


class ModelManager:
    """
    Clase para gestionar modelos ML.

    Estructura de guardado:
    /home/jovyan/work/models/<notebook_subpath>/<model_name>.joblib

    - notebook_subpath: subcarpeta relativa desde notebooks/ (obligatorio)
      Ejemplo: '5_problemas_clasificacion/3_clasificacion_cifar10'
    - overwrite: obligatorio al guardar, evita sobrescribir sin querer.
    """

    def __init__(self, notebook_subpath: str):
        if not notebook_subpath:
            raise ValueError(
                "Debes especificar 'notebook_subpath', "
                "p.ej. '5_problemas_clasificacion/3_clasificacion_cifar10'"
            )

        self.notebook_subpath = Path(notebook_subpath)

        # Ruta raíz del proyecto en el contenedor
        self.project_root = Path("/home/jovyan/work").resolve()

        # Carpeta base de modelos
        self.base_dir = self.project_root / "models"
        if not self.base_dir.exists():
            raise ValueError(
                f"La carpeta '{self.base_dir}' no existe. Debe existir en la raíz del proyecto."
            )

    def _get_model_dir(self) -> Path:
        """
        Obtiene el directorio donde se guardarán los modelos de este notebook.
        """
        model_dir = self.base_dir / self.notebook_subpath
        model_dir.mkdir(parents=True, exist_ok=True)
        return model_dir

    def save_model(self, model, model_name: str, overwrite: bool):
        """
        Guarda un modelo en el directorio correspondiente usando joblib.

        :param model: Modelo a guardar.
        :param model_name: Nombre del modelo (sin extensión).
        :param overwrite: Debe ser True para sobrescribir un modelo existente.
        """
        if not model_name or model is None:
            raise ValueError("Debe especificar 'model_name' y 'model'.")

        if overwrite not in [True, False]:
            raise ValueError(
                "Debes especificar explícitamente overwrite=True o overwrite=False"
            )

        model_dir = self._get_model_dir()
        model_path = model_dir / f"{model_name}.joblib"

        if model_path.exists() and not overwrite:
            raise FileExistsError(
                f"El modelo '{model_name}' ya existe en {model_dir}. "
                "Usa overwrite=True para sobrescribirlo."
            )

        joblib.dump(model, model_path)
        print(f"Modelo guardado en: {model_path}")

    def load_model(self, model_name: str):
        """
        Carga un modelo previamente guardado.
        """
        if not model_name:
            raise ValueError("Debe especificar 'model_name'")

        model_dir = self._get_model_dir()
        model_path = model_dir / f"{model_name}.joblib"

        if not model_path.exists():
            raise FileNotFoundError(
                f"No se encontró el modelo '{model_name}' en {model_dir}"
            )

        print(f"Modelo cargado desde: {model_path}")
        return joblib.load(model_path)
