import cv2
import numpy as np


# ---------------------------------------------------------
# Détection du centre de la cible
# ---------------------------------------------------------
def detect_center(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=80,
        param2=30,
        minRadius=10,
        maxRadius=80
    )

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        x, y, r = circles[0]
        return (x, y)

    return None


# ---------------------------------------------------------
# Détection du cercle extérieur (rayon max)
# ---------------------------------------------------------
def detect_cercle_exterieur(image, center):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=200,
        param1=100,
        param2=40,
        minRadius=80,
        maxRadius=300
    )

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        x, y, r = circles[0]
        return r

    return None


# ---------------------------------------------------------
# Détection des impacts (petits cercles)
# ---------------------------------------------------------
def detect_impacts(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 1.5)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=20,
        param1=50,
        param2=20,
        minRadius=5,
        maxRadius=20
    )

    impacts = []

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            impacts.append((x, y))

    return impacts



