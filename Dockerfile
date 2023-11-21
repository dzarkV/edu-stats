FROM node:18-alpine
# Para constuir imagen única
# Instala las dependencias necesarias
RUN apk update && \
    apk add --no-cache python3 py3-pip git curl && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools


# Configura la zona horaria
RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/America/Bogota /etc/localtime && \
    echo "America/Bogota" > /etc/timezone && \
    apk del tzdata

# Descarga el proyecto
WORKDIR /app
RUN git clone https://github.com/dzarkV/edu-stats.git

# Instala las dependencias del backend
WORKDIR /app/edu-stats/be-edu-stats
# Copia los archivos de credenciales
COPY . .
RUN pip install -r requirements.txt

# Instala las dependencias del frontend
WORKDIR /app/edu-stats/fe-edu-stats
RUN npm install

EXPOSE 9000
# Ejecuta ambos proyectos
CMD cd /app/edu-stats/be-edu-stats && python3 main.py & \
    cd /app/app/edu-stats/fe-edu-stats && npm run preview
