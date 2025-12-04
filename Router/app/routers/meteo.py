from fastapi import APIRouter
#Inizializzo il router
router = APIRouter()

#Definizione dell'endpoint per il meteo
@router.get("/meteo/{city_name}")
#definizione funzione per ottenere le informazioni sul meteo
def get_meteo(city_name:str):
    #ritorno le informazioni sul meteo e la città
    return {
        "city": city_name,
        "temperature_celsius": 18.5, 
        "conditions": "Soleggiato"
    }

