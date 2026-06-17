# Base de données des cibles officielles
CIBLES = {
    "C50": {
        "diametre_mm": 500,
        "anneaux": 10
    },
    "C10": {
        "diametre_mm": 170,
        "anneaux": 11
    },
    "10m_pistolet": {
        "diametre_mm": 155.5,
        "anneaux": 12
    },
    "25m_precision": {
        "diametre_mm": 500,
        "anneaux": 10
    },
    "50m_carabine": {
        "diametre_mm": 154.4,
        "anneaux": 12
    }
}

def identifier_cible(nb_anneaux_detectes, diametre_pixels):
    """
    Détecte automatiquement le type de cible.
    Ici, on commence simple : on se base surtout sur le nombre d’anneaux.
    """
    for nom, data in CIBLES.items():
        if data["anneaux"] == nb_anneaux_detectes:
            return nom

    # Fallback : si on ne trouve pas par anneaux, on choisit la plus proche en diamètre théorique
    diametres_mm = {nom: data["diametre_mm"] for nom, data in CIBLES.items()}
    cible_proche = min(diametres_mm, key=lambda c: abs(diametres_mm[c] - diametre_pixels))
    return cible_proche

def calculer_mm_par_pixel(diametre_mm, diametre_pixels):
    return diametre_mm / diametre_pixels

def convertir_impacts_mm(impacts_pixels, centre, mm_par_pixel):
    impacts_mm = []
    (cx, cy, _) = centre

    for (x, y, r) in impacts_pixels:
        dx = (x - cx) * mm_par_pixel
        dy = (y - cy) * mm_par_pixel
        impacts_mm.append((dx, dy))

    return impacts_mm
