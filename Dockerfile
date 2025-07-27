# Imagen a utilizar
FROM python:3.12-alpine

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dependencias del sistema
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev

# Crear espacio de trabajo
WORKDIR /app

# Mover dependencias.txt al contenedor
COPY dependencias.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r dependencias.txt

# Mover el resto del código al contenedor
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando por defecto al iniciar el contenedor
CMD ["uvicorn", "productos.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]