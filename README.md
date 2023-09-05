## Henry
### Proyecto Individual - Machine Learning Operations 
Mi nombre es Federico Molina, tengo 37 años, soy estudiante de Data Science en la Henry. También estudio Licenciatura en Ciencias de la Computación y de la Información y tengo el título de Técnico en Gastronomía y su Gerenciamiento. Vivo en San Juan, Argentina. Tengo un hijo de 5 años, que es mi compañero de muchas horas de estudio, de este apasionante mundo de la Computación, específicamente de mi nueva pasión que es la Ciencia de Datos.
##Primera Parte
Transformaciones: Para este MVP no se te pide transformaciones de datos(aunque encuentres una motivo para hacerlo) pero trabajaremos en leer el dataset con el formato correcto. Puedes eliminar las columnas que no necesitan para responder las consultas o preparar los modelos de aprendizaje automático, y de esa manera optimizar el rendimiento de la API y el entrenamiento del modelo.
Feature Engineering: En el dataset user_reviews se incluyen reseñas de juegos hechos por distintos usuarios. Debes crear la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP con la siguiente escala: debe tomar el valor '0' si es malo, '1' si es neutral y '2' si es positivo. Esta nueva columna debe reemplazar la de user_reviews.review para facilitar el trabajo de los modelos de machine learning y el análisis de datos. De no ser posible este análisis por estar ausente la reseña escrita, debe tomar el valor de 1.
Desarrollo API: Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:
Debes crear las siguientes funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@
