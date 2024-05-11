# Usa la imagen base de Python
FROM python:3.10-slim

WORKDIR /app
#Copiar de la carpeta de requirements
COPY ./requirements.txt .
#Instala y actualiza el PIP
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
#Indicas que copie de raiz todos los archivos
COPY . .
#Comando que va ejecutar para correr el servidor
CMD ["python3", "src/main.py"]