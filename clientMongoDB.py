from pymongo import MongoClient

def mongoClient():
    try:
        url="mongodb://localhost:27017/"
        return  MongoClient(url).peliculas
    except Exception as e :
        result={"status":-1, "error":f'{e}'}
