## Henry
### Proyecto Individual - Machine Learning Operations 
Mi nombre es Federico Molina, tengo 37 años, soy estudiante de Data Science en la Henry. También estudio Licenciatura en Ciencias de la Computación y de la Información y tengo el título de Técnico en Gastronomía y su Gerenciamiento. Vivo en San Juan, Argentina. Tengo un hijo de 5 años, que es mi compañero de muchas horas de estudio, de este apasionante mundo de la Computación, específicamente de mi nueva pasión que es la Ciencia de Datos.
## Primera Parte
- Data Engineering: debíamos asumir el rol de un Data Engineer. Se nos daba tres bases de datos de videojuegos de Steam en formato .gzip y debíamos llevar a cabo ciertas transformaciones para luego poder realizar algunas consultas a modo de prueba. Luego, procedemos a cargar los datos donde corresponda.
- Feature Engineering: en el dataset de reseñas debíamos crear una columna aplicando análisis de sentimiento con Procesamiento de Lenguaje Natural.
- Desarrollo API: teníamos que disponibilizar los datos de la empresa usando el framework FastAPI, creando 6 funciones consumibles en una API para que puedan ser consultadas.

## Segunda Parte
- Análisis exploratorio de los datos (EDA): es momento de analizar las relaciones que hay entre las variables del dataset, y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior.
- Modelo de aprendizaje automático: armar un sistema de recomendación. Hay dos propuestas de trabajo: en la primera, el modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar sea ese ítem al resto, se recomiendan otros. Aquí el input es un juego y el output es una lista de juegos recomendados. La otra propuesta para el sistema de recomendación debe aplicar el filtro user-item, esto es tomar un usuario, se encuentran usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.
Yo elegí la primera propuesta, así que debo crear una función que, ingresando un id de producto, se debe recibir una lista con 5 juegos recomendados similares al ingresado.
