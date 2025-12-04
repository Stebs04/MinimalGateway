from fastapi import FastAPI
#importo il modulo del meteo
from Router.app.routers import meteo
#Importo il modulo del pokemon
from Router.app.routers import pokemon

#Iniziallizo l'applicazione
app = FastAPI()

#includo il router del meteo
app.include_router(meteo.router) #meteo.router intende l'oggetto router dentro il file meteo
app.include_router(pokemon.router) 

@app.get("/")
def read_root():
    return{"message": "API GateWay attivo!!"}

