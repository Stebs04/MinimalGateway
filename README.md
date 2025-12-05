# 🚀 Minimal API Gateway con FastAPI

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Fast%20%26%20Modern-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

Questo progetto è un **API Gateway modulare** sviluppato con Python e
**FastAPI**.\
L'obiettivo è dimostrare un'architettura backend **pulita**,
**scalabile** e facilmente estendibile.

------------------------------------------------------------------------

## 📋 Funzionalità

-   **☁️ Meteo API** -- dati meteo simulati basati sul nome città\
-   **⚡ Pokémon API** -- informazioni simulate su un Pokémon specifico\
-   **🔒 Crypto API** -- hashing tramite `sha256`, `sha512`, `md5`\
-   **🔤 Utilities API** -- analisi testo: inversione, conteggio
    parole/caratteri

------------------------------------------------------------------------

## 🛠️ Tecnologie Utilizzate

-   Python 3.x\
-   FastAPI\
-   Uvicorn\
-   Pydantic\
-   Hashlib

------------------------------------------------------------------------

## 📂 Struttura del Progetto

``` text
📦 MinimalGateway
├── 📂 app
│   ├── 📂 routers
│   │   ├── crypto.py
│   │   ├── meteo.py
│   │   ├── pokemon.py
│   │   └── utilities.py
│   └── __init__.py
├── main.py
└── requirements.txt
```

------------------------------------------------------------------------

## 🚀 Installazione

``` bash
git clone https://github.com/tuo-username/minimal-gateway.git
cd minimal-gateway
```

### Crea ambiente virtuale

``` bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Installa dipendenze

``` bash
pip install fastapi uvicorn
```

### Avvia server

``` bash
uvicorn main:app --reload
```

Documentazione API: `http://127.0.0.1:8000/docs`

------------------------------------------------------------------------

## 📡 Endpoints API

### Meteo (GET) `/meteo/{city_name}`

Dati meteo simulati.

### Pokémon (GET) `/pokemon/{pokemon_name}`

Scheda Pokémon simulata.

### Hashing (POST) `/crypto/hash`

``` json
{
  "text_to_hash": "TuoTestoQui",
  "algorithm": "sha256"
}
```

### Analisi Testo (POST) `/utils/analyze`

``` json
{
  "text": "Esempio di frase"
}
```

------------------------------------------------------------------------

## 📜 Licenza

Rilasciato sotto licenza MIT.
