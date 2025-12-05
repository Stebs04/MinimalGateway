from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ReverseText(BaseModel):
    text: str

@router.post("/utilities/analyze")
def reverse_string(payload: ReverseText):
    reverse_text = payload.text[::-1]
    wordcount = len(payload.text.split())
    charcount = len(payload.text)
    return {
        "Reversed Text": reverse_text,
        "Word Count": wordcount,
        "Char count": charcount
    }