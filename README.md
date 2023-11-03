 # PI_MLOps_01 

  

  # Introducción 

📌 Para este proyecto se nos proporciona un conjunto de tres archivos de steam (Steam es una plataforma de distribución digital de videojuegos desarrollada por Valve Corporation) para poder trabajar en ellos y crear un Producto Minimo Viable (MVP), que contiene una la implementaciónde una API  y con un modelo de Machine Learning. los datos provienen de los archivos siguientes: 

  

steam_games: información relacionada a los juegos dentro de la plataforma Steam. Por ejemplo: Nombre del juego, género, fecha de lanzamiento, entre otras. 

  

user_reviews: información que detalla las reseñas realizadas por los usuarios de la plataforma Steam. 

  

user_items: información acerca de la actividad de los usuarios dentro de la plataforma Steam. 

  

Para entender el detalle de cada uno de los datasets, siga el siguiente enlace: [Data](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj),  

  

# Contexto 

Steam es una plataforma de distribución digital y comunidad de jugadores líderes en la industria de los videojuegos. Desarrollado por Valve Corporation, Steam ofrece a los usuarios una amplia gama de juegos para PC y otras plataformas. También es conocido por su sólida infraestructura de actualización y gestión de juegos, así como por su plataforma de desarrollo de juegos Steamworks, que brinda a los desarrolladores herramientas para crear y publicar juegos en la plataforma. Steam ha sido un pionero en la distribución digital de videojuegos y ha desempeñado un papel fundamental en la evolución de la industria de los videojuegos en línea. 

  

# Desarrollo  

En esta fase del proyecto se realiza la extracción de datos, a fin de familiarizarse con ellos y comenzar con la etapa de limpieza de datos que }nos permita el correcto entedimiento y lectura del archivo a fin de lograr los objetivos. Terminada la limpieza se generará el conjunto de datos para la siguiente fase, estos se guardaron en formato parquet. 

  

Para revisar en detalle el trabajo realizado, les dejo el siguiente enlace: [ETL_items](https://github.com/rafaelalvarez702/PI_MLOps_01/blob/main/ETL_items.ipynb),  [ETL_reviews](https://github.com/rafaelalvarez702/PI_MLOps_01/blob/main/ETL_reviews.ipynb), [ETL_Steam_games](https://github.com/rafaelalvarez702/PI_MLOps_01/blob/main/ETL_steam_games.ipynb) 

  

# Ingeniería de características 

El proyecto incluye el desarrollo de un modelo de análisis de sentimientos aplicado a los comentarios de los usuarios de juegos. Este modelo se desarrolla sobre el conjunto de datos user_reviews valiendonos de la librería TextBlob que  es parte de una biblioteca de procesamiento de lenguaje natural (NLP). 

Adicionalmente se preparan los conjuntos de datos necesarios para el desarrollo de algunas funciones y el modelo de Machine Learning. 

  

# Funciones a realizar 

def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género. 

Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013} 

  

def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año. 

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]} 

  

def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales) 

Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}] 

  

def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos) 

Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}] 

  

def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. 

Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278} 

Adjunto el cuaderno en el siguiente enlace:  [Funciones y EDA](https://github.com/rafaelalvarez702/PI_MLOps_01/blob/main/funciones_api.ipynb) 

# Modelamiento (Machine Learning)
En este paso, desarrollamos el modelo de aprendizaje automático utilizando los datos preparados anteriormente. Como base para el mismo se utiliza el conjunto de datos steam_games. 

def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

# API y Render

link al entorno web de la api realizado para poder realizar consultas: [Despliegue](https://rafaelalvarez702-pi-mlops-01-hdhw.onrender.com/docs) 

  

VIDEO 

link al video del proyecto y sus funciones: [Presentacion](https://rafaelalvarez702-pi-mlops-01-hdhw.onrender.com/docs)
