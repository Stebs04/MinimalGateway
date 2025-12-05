from fastapi import FastAPI
#importo il modulo del meteo
from Router.app.routers import meteo
#Importo il modulo del pokemon
from Router.app.routers import pokemon
#Importo il modulo crypto
from Router.app.routers import crypto
#Importo il modulo utilities
from Router.app.routers import utilities

#Iniziallizo l'applicazione
app = FastAPI()

#includo il router del meteo
app.include_router(meteo.router) #meteo.router intende l'oggetto router dentro il file meteo
app.include_router(pokemon.router)
app.include_router(crypto.router)
app.include_router(utilities.router)

@app.get("/")
def read_root():
    return{"message": "API GateWay attivo!!"}

