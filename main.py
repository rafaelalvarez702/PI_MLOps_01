


#librerías
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# intanciamos la app
app = FastAPI()

# cargamos los dataframes para las funciones de la API

df_s_analisis = pd.read_parquet("Datos/df_s_analisis.parquet")
df_PlayTimeGenre = pd.read_parquet("Datos/df_PlayTimeGenre.parquet")
df_UserForGenre= pd.read_parquet("Datos/df_UserForGenre.parquet")
df_UserRecommend = pd.read_parquet("Datos/df_UserRecommend.parquet")
df_sentiment_analysis = pd.read_parquet("Datos/df_sentiment_analysis.parquet")
df_r_juego= pd.read_parquet("Datos/df_r_juego.parquet")


@app.get("/")
def pagppal():
    return {"Bienvenido"}

#FUNCION 1
@app.get( "/PlayTimeGenre/{genero}")
async def PlayTimeGenre( genero : str ):
    
    '''Esta funcion debe devolver año con mas horas jugadas para dicho género.
    usando como parametro el genero.
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}'''
 
    data= df_PlayTimeGenre[df_PlayTimeGenre['genres'] == genero]
    # Encontrar el año con más horas jugadas
    año_horas = data.groupby('Año')['playtime_forever'].sum().idxmax(0)
    return {f"Año de lanzamiento con más horas jugadas para {genero}": año_horas}

#FUNCION 2
@app.get( "/UserForGenre/{genero}")
async def UserForGenre( genero : str ):

    '''
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
    Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, 
    "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
    '''
    data= df_UserForGenre[df_UserForGenre['genres'] == genero]
    usuarios_horas = data.groupby('user_id')['playtime_forever'].sum().idxmax(0)
    horas_por_año = data.groupby('Año')['playtime_forever'].sum().reset_index()
    resultado = {
        "Usuario con más horas jugadas para " + genero: usuarios_horas,
        "Horas jugadas": [{"Año": int(row['Año']), "Horas": int(row['playtime_forever']/60)} for index, row in horas_por_año.iterrows()]
    }
    
    return resultado

#FUNCION 3
@app.get( "/UsersRecommend/{anio}")
async def UsersRecommend( anio : int ):
    
    '''Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. 
    (reviews.recommend = True y comentarios positivos/neutrales)
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]'''
    
       # Filtra el DataFrame para el año dado y los criterios especificados.
    juegos_filtrados = df_UserRecommend[(df_UserRecommend['Año'] == anio) & (df_UserRecommend['recommend'] == True) & 
                                        ((df_UserRecommend['sentiment_analisis'] == 2) | (df_UserRecommend['sentiment_analisis'] == 1))]

    # Agrupa por el nombre del juego y suma las recomendaciones y sentimientos.
    ranking = juegos_filtrados.groupby('app_name').agg({'recommend': 'sum', 'sentiment_analisis': 'sum'})

    # Calcula una puntuación que combina recomendaciones y sentimientos.
    ranking.loc[:, 'puntuacion'] = ranking['recommend'] + ranking['sentiment_analisis']

    # Ordena el ranking por la puntuación en orden descendente.
    ranking_ordenado = ranking.sort_values(by='puntuacion', ascending=False)

    # Toma los primeros 3 juegos del ranking.
    top3_juegos = ranking_ordenado.head(3)

    # Crea el formato de retorno deseado.
    resultado = [{"Puesto {}: {}".format(i + 1, juego)} for i, juego in enumerate(top3_juegos.index)]

    return resultado


