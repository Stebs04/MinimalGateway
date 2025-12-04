from fastapi import APIRouter

router = APIRouter()

@router.get("/pokemon/{pokemon_type}")
def get_pokemon(pokemon_type: str):
    return {
        "Pokemon Name": "Pikachu",
        "Pokemon Entry": "Un topo elettrico",
        "Pokemon Type": pokemon_type,
        "height_m": 0.4,
        "weight_kg": 6.0
    }