# Base CPU con TensorFlow y JupyterLab
FROM jupyter/tensorflow-notebook:latest

# Directorio de trabajo
WORKDIR /home/jovyan/work

# Variables de entorno
ENV CONDA_ENV_NAME=ia_bigdata
ENV KERNEL_DISPLAY_NAME="IA & BigData"

# Crear entorno Conda con librerías básicas + kernel
RUN conda create -y -n $CONDA_ENV_NAME python=3.11 \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    ipykernel \
    jupyterlab \
 && conda clean --all -y \
 # Instalar TensorFlow y keras-tuner vía pip (rápido)
 && /opt/conda/bin/conda run -n $CONDA_ENV_NAME pip install tensorflow==2.20 keras-tuner \
 # Registrar kernel en JupyterLab
 && /opt/conda/bin/conda run -n $CONDA_ENV_NAME python -m ipykernel install --user --name $CONDA_ENV_NAME --display-name "$KERNEL_DISPLAY_NAME"
 
# Exponer puerto de Jupyter
EXPOSE 8888

# Arrancar JupyterLab
CMD ["start-notebook.sh", "--LabApp.token=''"]
