''' Aquí hacemos el esquema que nos pasa a formato JSON los datos que le pasamos'''

'''Primero definimos el esquema para una sola film'''
def schemaFilm(film)->dict:
    return {
        "id": str(film["_id"]),
        "tittle": film['title'],
        "director": film['director'],
        "year":film['year'],
        "genre":film['genre'],
        "rating":film['rating'],
        "country":film['country']
    }
''' Ahora definimos el esquema para todas las films'''
def schemaFilms(films)->dict:
    return[schemaFilm(film) for film in films]