from fastapi import FastAPI
from repositoriosFilms import *
from schema_films import *
from clientMongoDB import mongoClient
from datetime import datetime
from  pymongo import *
from modelFilm import *

app = FastAPI()



# newCollection = mongoClient()
# current_dateTime = datetime.now()
# newDocument = {
#    "title": "El Padrino",
# 	 "director": "Francis Ford Coppola",
# 	 "year": 1972,
# 	 "genre": "Crimen",
# 	 "rating":9.9 ,
# 	 "country": "United States",
#    "created_at": current_dateTime,
#    "update_at": current_dateTime,
# }
# mongoClient().films.insert_one(newDocument)

''' A continuación los controladores con sus rutas para hacer las peticiones HTTP mediante FastAPI'''
 
'''Acordarse de usar uvicorn main:app --reload (en el directorio donde se encuentra main.py) para ejecutar el servidor en local 
La ruta para Swagger es : urlLocalHost/docs '''

'''Obtener todos los films'''
@app.get("/films/")
def getFilms():
    try:
        films = findAllFilms()
        films_json = schemaFilms(films)
        return films_json
    except Exception as e:
        print(f'Error: {e}')

'''Obtener el film especifico por su id'''
@app.get("/filmId/{id}")
def getFilmsId(id: str):
    try:
        film = findFilmById(id) 
        film_json = schemaFilm(film) 
        return film_json
    except Exception as e:
        print(f'Error: {e}')

#Para introducir una nueva pelicula
@app.post("/film/")
def insertFilm(film:Film):
        return insertOnefilm(film)

#Para modificar una pelicula por su ID
@app.put("/filmUpdate/{id}")
def putFilm(id, film:Film):
    return updateFilm(id, film)

#Eliminar una pelicula por su ID
@app.delete("/filmDelete/{id}")
def borrarFilm(id):
    return deleteFilm(id)

#Consultas avanzadas
#Lista según genero 
@app.get("/filmGenreList/{genre}")
def filmsByGenre(genre):
    return getFilmsByGenre(genre)

#Lista ordenada ascendente o descendente :
@app.get("/filmsByOrder/{field}/{order}")
def getFilmsByOrderField(field: str, order:str):
    return getFilmsByOrder(field, order)

#Lista de documentos con el número total de documentos según el límite
@app.get("/filmsByLimit/")
def getLimitedFilms(limit: int):
    return getFilmsByLimit(limit)