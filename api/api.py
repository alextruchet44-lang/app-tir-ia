from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import cv2
import numpy as np

app = FastAPI()

# CORS (important pour Flutter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Route obligatoire pour Render (sinon Render coupe ton service)
@app.get("/")
def home():
    return {"status": "API OK", "message": "Service en ligne et opérationnel"}

# 🔥 Route d'analyse (celle que ton app Flutter appelle)
@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    # Lecture du fichier envoyé
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "Impossible de lire l'image"}

    # ---------------------------------------------------------
    # 🔥 Exemple d'analyse (à remplacer par ton vrai traitement)
    # ---------------------------------------------------------

    height, width = img.shape[:2]

    # Exemple : centre fictif
    center = {"x": width / 2, "y": height / 2}

    # Exemple : un impact fictif
    shots = [
        {"x": width * 0.4, "y": height * 0.6, "score": 8.5},
        {"x": width * 0.55, "y": height * 0.45, "score": 9.2},
    ]

    # Exemple : score total
    total_score = sum(s["score"] for s in shots)

    # Exemple : groupement fictif
    grouping = 12.7

    return {
        "center": center,
        "shots": shots,
        "total_score": total_score,
        "grouping": grouping,
    }

# 🔥 Lancement local (ne sert pas sur Render)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
