# Proyecto Individual - Machine Learning Operations Engineer
  Mi nombre es Federico Molina, soy Data Scientist y este es mi primer proyecto de Ciencias de Datos. Steam, la plataforma multinacional de videojuegos, necesita crear un sistema de recomendación de videojuegos para usuarios.

![](https://github.com/federicomolina86/Proyecto-MLOps-Engineer/blob/main/src/Steam_logo.jpg)

## Primera Parte
- Data Engineering (proceso de ETL): a partir de tres bases de datos sobre los juegos, sus reseñas y características, y luego de la carga de las mismas, realicé ciertas transformaciones para dejarlas en condiciones óptimas, sin faltantes de datos ni columnas innecesarias. Todo este proceso lo realicé usando el lenguaje `Python` y la librería `Pandas`. 
- Feature Engineering: en el dataset de reseñas cree una columna aplicando análisis de sentimiento con Procesamiento de Lenguaje Natural (NLP) usando la librería `NLTK`. El proceso dejaba como resultado los valores "2" para reseñas positivas, "0" para negativas y "1" para las neutrales o inexistentes.
- Desarrollo API: luego disponibilicé los datos de la empresa usando el framework `FastAPI`, creando 6 funciones consumibles en una API para que puedan ser consultadas. Estas funciones fueron solicitadas por la misma empresa.

## Segunda Parte
- Análisis exploratorio de los datos (EDA): en esta parte analicé las relaciones que habían entre las variables de los dataset, y busqué patrones interesantes que valieran la pena explorar.
- Modelo de aprendizaje automático: armé un sistema de recomendación con la librería `Scikit-Learn`, usando una relación ítem-ítem (en base a que tan similar sea ese ítem al resto, se recomiendan otros). El input es un juego y el output es una lista de juegos recomendados. Luego añadí este modelo a la API para que también pueda ser consultado.

## Contenido del Repositorio
  - Notebook del ETL-EDA y otro del Modelo de ML dentro de la carpeta'ETL-EDA-ML'.
  - Los 3 datasets con sus respectivas transformaciones en formato 'csv' y 'parquet'.
  - Archivo 'main.py', que incluye las 6 funciones a disponibilizar en la API, cada una con su correspondiente decorador.
  - Archivo '.gitignore' y 'requirements.txt', que incluye todas las librerías utilizadas.
  - README.md
  - Carpeta 'src' que incluye las imágenes del README.
