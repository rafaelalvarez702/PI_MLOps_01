  # PI_MLOps_01

  # Introducción
 📌 Para este proyecto se nos proporciona un conjunto de tres archivos de steam (Steam es una plataforma de distribución digital de videojuegos desarrollada por Valve Corporation) para poder trabajar en ellos y crear un Producto Minimo Viable (MVP), que contiene una la implementaciónde una API  y con un modelo de Machine Learningque asu vez realizar análisis de sentimientos a partir de los comentarios de los usuarios y un sistema de recomendación de videojuegos para la plataforma. los datos provienen de los archivos siguientes:
 
 steam_games: información relacionada a los juegos dentro de la plataforma Steam. Por ejemplo: Nombre del juego, género, fecha de lanzamiento, entre otras.

user_reviews: información que detalla las reseñas realizadas por los usuarios de la plataforma Steam.

user_items: información acerca de la actividad de los usuarios dentro de la plataforma Steam.

Para entender el detalle de cada uno de los datasets, siga el siguiente enlace: [Data](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj), 

# Contexto
Steam es una plataforma de distribución digital y comunidad de jugadores líderes en la industria de los videojuegos. Desarrollado por Valve Corporation, Steam ofrece a los usuarios una amplia gama de juegos para PC y otras plataformas. También es conocido por su sólida infraestructura de actualización y gestión de juegos, así como por su plataforma de desarrollo de juegos Steamworks, que brinda a los desarrolladores herramientas para crear y publicar juegos en la plataforma. Steam ha sido un pionero en la distribución digital de videojuegos y ha desempeñado un papel fundamental en la evolución de la industria de los videojuegos en línea.

# Desarrollo 
En esta fase del proyecto se realiza la extracción de datos, a fin de familiarizarse con ellos y comenzar con la etapa de limpieza de datos que no nos permita el correcto entedimiento y lectura del archivo a fin de lograr los objetivos. Terminada la limpieza se generará el conjunto de datos para la siguiente fase. Para este caso se comprimieron un formatoparquet.

Para revisar en detalle el trabajo realizado, les dejo el siguiente enlace: [ETL_items](https://github.com/rafaelalvarez702/PI_MLOps_01/blob/main/ETL_items.ipynb),  [ETL_reviews](https://github.com/rafaelalvarez702/PI_MLOps_01/blob/main/ETL_reviews.ipynb), [ETL_Steam_games](https://github.com/rafaelalvarez702/PI_MLOps_01/blob/main/ETL_steam_games.ipynb)

Ingeniería de características
Una vez realizado el etl, con mis datos limpios, procedi a hacer el proceso de ingeniería de características , donde tuve que crear análisis de sentimiento y varias funciones más que se pidieron, una vez realizado todo que tuve que crear una API local que me permitió interactuar con las funciones realizadas con los datos, utilice render para levantar un servicio web en línea, donde cualquier persona puede interactuar con los datos y obtener información.💥

Funciones a realizar
userdata(User_id: str): Esta función toma como entrada el ID de un usuario y devuelve la cantidad de dinero gastado por ese usuario, el porcentaje de recomendación basado en las revisiones (reviews.recommend) y la cantidad de items relacionados con ese usuario .

countreviews(AAAA-MM-DD y AAAA-MM-DD: str): Esta función toma dos fechas en formato AAAA-MM-DD como entrada y devuelve la cantidad de usuarios que realizaron reviews entre esas dos fechas, así como el porcentaje de Recomendación basada en las revisiones realizadas durante ese período.

género(género: str): Esta función toma un género como entrada y devuelve la posición en la que se encuentra ese género en un ranking analizado bajo la columna PlayTimeForever.

userforgenre(género: str): Esta función toma un género como entrada y devuelve los cinco usuarios con más horas de juego en ese género, junto con sus URL de usuario (del juego) y sus ID de usuario.

desarrollador(desarrollador: str): Esta función toma como entrada el nombre de una empresa desarrolladora y devuelve la cantidad de items (juegos o contenido) producidos por esa empresa por año, así como el porcentaje de contenido gratuito en esos items.

sentiment_analysis(año: int): Esta función toma un año como entrada y devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentran categorizados con un análisis de sentimiento para ese año en particular.

API
link al entorno web de la api realizado para poder realizar consultas: https://prueba-api-gj31.onrender.com/docs#

VIDEO
link al video explicativo del proyecto y sus funciones: https://www.youtube.com/watch?v=-e8pdmXf3C4
