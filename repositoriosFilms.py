''' Aquí se definen todas las querys que haremos sobre la BD de Mongo'''
from clientMongoDB import mongoClient
import pymongo
import json
from bson import ObjectId
from schema_films import *
from fastapi import FastAPI, HTTPException
from datetime import *

'''Variable que usamos para modificar los update_at or created_at'''
current_datatime=datetime.now()

'''Lista de funciones que utilizamos para hacer el CRUD sobre MongoDB y son las funciones que usamos en main.py(Controladores)'''
def findAllFilms():
    client = mongoClient().films
    return list(client.find())

def findFilmById(id:str):
    client = mongoClient().films
    resultado = client.find_one({"_id": ObjectId(id)})
    if resultado:
        return resultado
    else:
        "Documento no encontrado"

def insertOnefilm(film):
    try:
        film={ 
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre":  film.genre,
            "rating":  film.rating,    
            "country":  film.country,
            "created_at": current_datatime,
            "updated_at":current_datatime
            }
        client = mongoClient().films
        insertedFilm = client.insert_one(film)
        if insertedFilm.inserted_id:
            return{"status":1,"message":"Inserción con éxito","film_id":str(insertedFilm.inserted_id)}
        else:
            return {"status":-1,"message":"Inserción no exitosa"}
    except Exception as e:
        return{"status":-1,"message":f'Hay un error: {e}'}

def updateFilm(id,film):
    try:
        filmToUpdate={
            "$set":{
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre":  film.genre,
            "rating":  film.rating,    
            "country":  film.country,
            "updated_at":current_datatime 
            }
        }
        client = mongoClient().films
        resultado = client.update_one({"_id":ObjectId(id)},filmToUpdate)
        if resultado.modified_count == 1 :
                return{"status":1,"message":"Modificación con éxito"}
        else:
            return {"status":-1,"message":"Modificación no exitosa"}
    except Exception as e:
        return{"status":-1,"message":f'Hay un error: {e}'}

def deleteFilm(id):
    try:
        client = mongoClient().films
        resultado = client.delete_one({"_id": ObjectId(id)})
        if resultado.deleted_count == 1:
            return {"status": 1, "message": "Film borrada con éxito"}
        else:
            return {"status": -1, "message": "No se ha eliminado ninguna película que se corresponda con ese ID"}
    except Exception as e:
        return {"status": -1, "Error conexión": f'Hay un error: {e}'}
    
def getFilmsByGenre(genre):
    try:
        client = mongoClient().films
        filmsByGenre = client.find({"genre":genre})
        filmsByGenre_dict = schemaFilms(filmsByGenre)
        if filmsByGenre:
            return {"status": 1, "data":filmsByGenre_dict}
        else:
            return {"status": -1, "message": "No se han encontrado  películas que se corresponda con el género seleccionado"}
    except Exception as e:
        return {"status": -1, "Error conexión": f'Hay un error: {e}'}

def getFilmsByOrder(field: str, order: str):
    try:
        if order not in ["asc", "desc"]:
            return {"status": -1, "message": "Parámetros erroneos , debes seleccionar 'asc' o 'desc'."}

        filtered_films = get_filtered_films(field, order)
        if filtered_films:
            return {"status": 1, "data": schemaFilms(filtered_films)}
        else:
            return {"status": -1, "message": "No hay películas según los filtros seleccionados."}
    except Exception as e:
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}

def get_filtered_films(field: str, order: str):
    client = mongoClient().films
    return client.find().sort(field, 1 if order == "asc" else -1)

def getFilmsByLimit(limit):
    try:
        client = mongoClient().films
        films_limited = client.find().limit(limit)
        if films_limited:
            return {"status": 1, "data": schemaFilms(films_limited)}
        else:
            return {"status": -1, "message": "No se encontraron películas para el límite seleccionado"}
    except Exception as e:
        return {"status": -1, "Error de conexión": f'Error: {e}'}
