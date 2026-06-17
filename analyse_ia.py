import cv2
import numpy as np
from session_tir import SessionTir
from image_tools import detect_impacts, detect_center, detect_cercle_exterieur


def analyser_cible(image_path):
    """
    Analyse complète d'une cible :
    - détection du centre
    - détection du cercle extérieur
    - détection des impacts
    - calcul du score
    """

    # Chargement de l'image
    image = cv2.imread(image_path)
    if image is None:
        print("Erreur : impossible de charger l'image.")
        return None

    # Détection du centre
    center = detect_center(image)
    if center is None:
        print("Centre non détecté.")
        return None

    # Détection du cercle extérieur (rayon max)
    rayon_exterieur = detect_cercle_exterieur(image, center)
    if rayon_exterieur is None:
        print("Cercle extérieur non détecté.")
        return None

    # Détection des impacts
    impacts = detect_impacts(image)
    if impacts is None or len(impacts) == 0:
        print("Aucun impact détecté.")
        return None

    # Création de la session
    session = SessionTir(
        calibre="4.5mm",
        distance="10m",
        impacts=impacts,
        centre=center,
        rayon_exterieur=rayon_exterieur
    )

    return session


