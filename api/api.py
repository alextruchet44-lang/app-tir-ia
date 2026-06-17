import sys
import os

# --- Permet à Python de trouver analyse_ia.py dans le dossier parent ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# -----------------------------------------------------------------------

from fastapi import FastAPI, UploadFile, File
from analyse_ia import analyser_cible
import uvicorn
import shutil

app = FastAPI()

@app.post("/analyser")
async def analyser_carton(file: UploadFile = File(...)):
    # Sauvegarde temporaire de l'image envoyée
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Analyse IA
    session = analyser_cible(temp_path)

    # Suppression du fichier temporaire
    os.remove(temp_path)

    if session is None:
        return {"success": False, "message": "Analyse impossible"}

    # Conversion en JSON
    return {
        "success": True,
        "score_total": session.score_total(),
        "impacts": session.impacts,
        "calibre": session.calibre,
        "distance": session.distance,
        "nb_impacts": session.nombre_impacts(),
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

