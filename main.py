from fastapi import FastAPI
import pandas as pd
from datetime import datetime

app = FastAPI()

items_df = pd.read_parquet('items.parquet')
reviews_df=pd.read_csv('reviews_with_sentiment.csv')
games_df=pd.read_csv('games_ultimo.csv')


#1
@app.get('/userdata/{user_id}')
def userdata(user_id: str):
    """
    Esta función recibe como parámetro el id de un usuario de Steam y luego
    calcula la cantidad de dinero gastado por el usuario, el porcentaje de 
    recomendaciones y la cantidad de items comprados por el mismo.
    """
    # Filtrar los items comprados por el usuario
    user_items = items_df[['user_id'] == user_id]
    
    user_spent_money = (user_items['items_count'] * games_df[items_df['user_id']]['price']).sum()

    recommend_percentage = (reviews_df[items_df['user_id'] == user_id]['recommend'].mean()) * 100
 
    total_items_count = items_df['items_count'].sum()

    return user_spent_money, recommend_percentage, total_items_count

#2
@app.get('/countreviews/{start_date, end_date}')
def countreviews(start_date, end_date: str):
    """
    Esta función toma como parámetro dos fechas, y cuenta la cantidad de usuarios que realizaron
    reseñas dentro del rango de fechas dado y calcula el porcentaje de recomendación
    """
    # Convertir las fechas de entrada en objetos datetime
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    filtered_reviews = [review for review in reviews_df if start_date <= review['date'] <= end_date]
    
    users = set()
    for review in filtered_reviews:
        users.add(review['user_id'])
    
    total_reviews = len(filtered_reviews)
    if total_reviews > 0:
        recommend_reviews = sum(1 for review in filtered_reviews if review['recommend'] == True)
        percentage_recommendation = (recommend_reviews / total_reviews) * 100
    else:
        percentage_recommendation = 0.0
    
    return len(users), percentage_recommendation

#3
@app.get('/genre/{genero}')
def genre(genero: str):
    """
    Esta función toma como parámetro un género de juegos y devuelve el puesto en el que 
    se encuentra sobre el ranking de los mismos analizado bajo la columna playtime_forever.
    """
    # Verificar que el género esté en el DataFrame
    if genero not in games_df.columns:
        return "Género no encontrado en el DataFrame games_df"

    # Filtrar los juegos del género especificado
    juegos_del_genero = games_df[genero] == 1

    # Filtrar los elementos relevantes en items_df
    items_del_genero = items_df[juegos_del_genero]

    # Ordenar los juegos de manera descendente
    items_del_genero = items_del_genero.sort_values(by=items_df['playtime_forever'], ascending=False)

    # Encontrar la posición del género en el ranking
    posición = (items_del_genero.index == genero).argmax() + 1

    return posición

#4
@app.get('/userforgenre/{genero}')
def userforgenre(genero: str):
    """
    Esta función toma como parámetro un tipo de género de juegos, y muestra el top 5 de usuarios
    con más horas de juego en el género dado, con su respectivo URL y su id.
    """
    # Filtrar juegos del género dado
    genero_column = games_df[genero] == 1
    juegos_del_genero = games_df[genero_column]['title']

    # Filtrar entradas de usuarios que hayan jugado a juegos del género
    usuarios_del_genero = items_df[items_df['item_id'].isin(juegos_del_genero)]

    # Calcular las horas totales jugadas por usuario
    horas_por_usuario = usuarios_del_genero.groupby('user_id')['playtime_forever'].sum()

    # Ordenar los usuarios por horas jugadas en orden descendente
    top_usuarios = horas_por_usuario.sort_values(ascending=False).head(5)

    # Obtener las URL de usuario y user_id para los usuarios principales
    usuarios_principales = items_df[items_df['user_id'].isin(top_usuarios.index)][['user_id', 'user_url']]

    return usuarios_principales

#5
@app.get('/developer/{desarrollador}')
def developer(desarrollador: str):
    """
    Esta función toma como parámetro un desarrollador de videojuegos, devuelve la
    cantidad de juegoss y porcentaje de contenido Free por año según la empresa.
    """
    # Filtrar el DataFrame para obtener solo las filas del desarrollador dado y precio Free
    filtered_df = games_df[(games_df['developer'] == desarrollador) & (games_df['price'] == 0.0)]
    
    # Inicializar un diccionario para almacenar los resultados
    results = {}
    
    # Obtener la lista de años únicos en el DataFrame filtrado
    years = filtered_df['release_year'].unique()
    
    # Calcular las estadísticas para cada año
    for year in years:
        # Filtrar el DataFrame por año
        year_df = filtered_df[filtered_df['release_year'] == year]
        
        # Calcular la cantidad de elementos de precio Free en este año
        count = len(year_df)
        
        # Calcular el porcentaje en relación con el total de elementos desarrollados en este año
        total_count = len(games_df[games_df['developer'] == desarrollador])
        percentage = (count / total_count) * 100 if total_count > 0 else 0
        
        # Agregar los resultados al diccionario
        results[year] = (count, percentage)
    
    return results

#6
@app.get('/sentiment_analysis/{año}')
def sentiment_analysis(año: int):
"""
Esta función toma como parámetro valores analizados por análisis de sentimiento, 
y según el año de lanzamiento, devuelve una lista con la cantidad de registros de reseñas 
de usuarios que se encuentren categorizados con un análisis de sentimiento.
"""
    
    # Filtrar el dataframe de juegos por el año especificado
    juegos_del_año = games_df[games_df['release_year'] == año]

    # Unir el dataframe de juegos con el dataframe de reseñas
    juegos_y_reseñas = pd.merge(juegos_del_año, reviews_df, on='id')

    # Contar la cantidad de registros de reseñas con cada categoría de sentimiento
    sentimiento_positivo = len(juegos_y_reseñas[juegos_y_reseñas['sentiment_analysis'] == 2])
    sentimiento_neutral = len(juegos_y_reseñas[juegos_y_reseñas['sentiment_analysis'] == 1])
    sentimiento_negativo = len(juegos_y_reseñas[juegos_y_reseñas['sentiment_analysis'] == 0])

    # Crear una lista con los resultados
    resultados = [sentimiento_negativo, sentimiento_neutral, sentimiento_positivo]

    return resultados


#Función de recomendación
@app.get('/recommend_games/{game_id}')
def recommend_games(game_id):
    """
    Esta función toma como parámetro un id de juegos y a través de un modelo
    de recomendación, devuelve 5 juegos similares
    """
    # Encontrar el ID del juego en base al título
    game_title = games_df[games_df['id'] == game_id]['title'].values[0]

    # Obtener las puntuaciones de similitud del juego específico
    game_similarity_scores = cosine_similarity[game_id]

    # Ordenar los juegos por similitud descendente
    recommended_game_ids = game_similarity_scores.sort_values(ascending=False).index[1:6]

    # Obtener los títulos de los 5 juegos recomendados
    recommended_games = games_df[games_df['id'].isin(recommended_game_ids)]['title']

    return recommended_games
