from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

@app.get("/")
async def hello_word():
    return {"hello": "world"}

@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return {"component_id": component_id}

#optional parameter
@app.get("/component/")
async def read_component(number: int, text: Optional[str]):
    return {"number": number, "text": text}

@app.get("/calculatrice/{nombre_un}/{nombre_deux}")
async def calculatrice(nombre_un: int, nombre_deux: int):
    return {"resultat": nombre_un * nombre_deux}

#creation d'une classe Enum
class ModelName(str, Enum):
    michel = "michel"
    alex = "alex"
    bobo = "bobo"

@app.get("/nom/{nom}")
async def model(nom: ModelName):
    if nom == ModelName.michel:
        return f"Bonjour {nom}, heureux de vous revoir :)"
    
    if nom == ModelName.alex:
        return f"Hey {nom} comment vas tu ?"
    
    return f"Je suis le commandant {nom}."



#query parameter type conversion
@app.get("/items/{items_id}")
async def read_item(items_id: str, q: Optional[str] = None, short: bool = False):
    item = {"items_id": items_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"msg": "la valeur est vrai"})


#TP calcultrice
class Calcul(str, Enum):
    addition = "addition"
    soustraction = "soustraction"
    multiplication = "multiplication"
    division = "division"

@app.get("/calcul/{entier_un}/{entier_deux}")
async def calcul(operateur: Calcul, entier_un: int, entier_deux: int):
    if operateur == Calcul.addition:
        return f"l'{operateur} de {entier_un} et {entier_deux} donne {entier_un + entier_deux}"

    if operateur == Calcul.soustraction:
        if entier_deux > entier_un:
            return f"la {operateur} de {entier_deux} et {entier_un} donne {entier_deux - entier_un}"
        return f"la {operateur} de {entier_un} et {entier_deux} donne {entier_un - entier_deux}"

    if operateur == Calcul.multiplication:
        return f"la {operateur} de {entier_un} et {entier_deux} donne {entier_deux * entier_un}"

    if operateur == Calcul.division:
        if (entier_un and entier_deux) != 0:
            return f"la {operateur} de {entier_un} et {entier_deux} donne {entier_un / entier_deux}"
        return f"Erreur division par zéro"



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)