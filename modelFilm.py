''' Hacemos el modelo del objeto con el que trabajaremos en MongoDB'''
from datetime import date
from pydantic import BaseModel

class Film(BaseModel):
    title:str
    director:str
    year:int
    genre:str
    rating:int
    country:str

