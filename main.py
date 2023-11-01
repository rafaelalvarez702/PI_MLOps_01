


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
 
    data= df_PlayTimeGenre[df_PlayTimeGenre['genres'] == genero]
    # Encontrar el año con más horas jugadas
    año_horas = data.groupby('Año')['playtime_forever'].sum().idxmax(0)
    
   
    
    return {f"Año de lanzamiento con más horas jugadas para {genero}": año_horas}




