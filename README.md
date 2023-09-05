## Henry
### Proyecto Individual - Machine Learning Operations 
Mi nombre es Federico Molina, tengo 37 años, soy estudiante de Data Science en la Henry. También estudio Licenciatura en Ciencias de la Computación y de la Información y tengo el título de Técnico en Gastronomía y su Gerenciamiento. Vivo en San Juan, Argentina. Tengo un hijo de 5 años, que es mi compañero de muchas horas de estudio, de este apasionante mundo de la Computación, específicamente de mi nueva pasión que es la Ciencia de Datos.
##Primera Parte
- Data Engineering: debíamos asumir el rol de un Data Engineer. Se nos daba tres bases de datos de videojuegos de Steam en formato .gzip y debíamos llevar a cabo ciertas transformaciones para luego poder realizar algunas consultas a modo de prueba. Luego, procedemos a cargar los datos donde corresponda."
- Feature Engineering: en el dataset de reseñas debíamos crear una columna aplicando análisis de sentimiento con Procesamiento de Lenguaje Natural.
- Desarrollo API: teníamos que disponibilizar los datos de la empresa usando el framework FastAPI, creando 6 funciones consumibles en una API para que puedan ser consultadas.

Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables del dataset, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente 👀 ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Las nubes de palabras dan una buena idea de cuáles palabras son más frecuentes en los títulos, ¡podría ayudar al sistema de predicción! En esta ocasión vamos a pedirte que no uses librerías para hacer EDA automático ya que queremos que pongas en práctica los conceptos y tareas involucrados en el mismo. Puedes leer un poco más sobre EDA en este articulo

Modelo de aprendizaje automático:

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación. Para ello, te ofrecen dos propuestas de trabajo: En la primera, el modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto, se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello recomendamos aplicar la similitud del coseno. La otra propuesta para el sistema de recomendación debe aplicar el filtro user-item, esto es tomar un usuario, se encuentran usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron. En este caso el input es un usuario y el output es una lista de juegos que se le recomienda a ese usuario, en general se explican como “A usuarios que son similares a tí también les gustó…”. Deben crear al menos uno de los dos sistemas de recomendación (Si se atreven a tomar el desafío, para mostrar su capacidad al equipo, ¡pueden hacer ambos!). Tu líder pide que el modelo derive obligatoriamente en un GET/POST en la API símil al siguiente formato:

Si es un sistema de recomendación item-item:

def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
