# Base con CUDA + TensorFlow + Jupyter
FROM tensorflow/tensorflow:2.16.1-gpu-jupyter

# Directorio de trabajo
WORKDIR /home/jovyan/work

# Crear directorios esperados por los volúmenes
RUN mkdir -p /home/jovyan/work

# Dependencias necesarias para los notebooks
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    keras-tuner \
    kagglehub \
    imbalanced-learn \
    xgboost \
    statsmodels

# Exponer puerto de Jupyter
EXPOSE 8888

# Arrancar JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--ServerApp.token=", "--ServerApp.password="]
