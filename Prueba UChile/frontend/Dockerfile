# Establecer la imagen base
FROM node:latest

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar las dependencias del proyecto
RUN npm install

# Iniciar la aplicación React
CMD ["npm", "start"]