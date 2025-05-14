# Imagen base oficial de Python
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Expone el puerto 8080 (usado por Flask en Heroku y Docker)
EXPOSE 8080

# Comando para correr la app
CMD ["python", "Suma.py"]
