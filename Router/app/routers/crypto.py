from fastapi import APIRouter, HTTPException
from pydantic import BaseModel #Importo BaseModel da pydantic
import hashlib 

router = APIRouter()

class HashRequest(BaseModel): #Creo la classe HashRequest che eredita da base model
    text_to_hash: str
    algorithm: str

@router.post("/crypto/hash")
def calculate_hash(payload: HashRequest):
    if payload.algorithm == "sha256" :
            # Nota: .encode() trasforma la stringa in byte, .hexdigest() la ritrasforma in stringa leggibile
            risultato = hashlib.sha256(payload.text_to_hash.encode()).hexdigest()
    elif payload.algorithm == "sha512":
            risultato = hashlib.sha512(payload.text_to_hash.encode()).hexdigest()
    elif payload.algorithm == "md5":
            risultato = hashlib.md5(payload.text_to_hash.encode()).hexdigest()
    else: #Se l'algoritmo non è supportato 
             #Sollevo una eccezione HTTP
            raise HTTPException(status_code=400, detail="algoritmo non supporato")
    return {
        "text": payload.text_to_hash,
        "algorithm": payload.algorithm,
        "hashed value": risultato
    }
