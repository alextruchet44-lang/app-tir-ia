from datetime import datetime
import math

class SessionTir:
    def __init__(self, calibre: str, distance: int, zones=None):
        self.date = datetime.now()
        self.calibre = calibre
        self.distance = distance
        self.impacts = []

        self.zones = zones or [
            (10, 10),
            (20, 9),
            (30, 8),
            (40, 7),
            (50, 6),
            (60, 5),
            (70, 4),
            (80, 3),
            (90, 2),
            (100, 1),
        ]

    def ajouter_impact(self, x: float, y: float):
        self.impacts.append((x, y))

    def nombre_impacts(self):
        return len(self.impacts)

    def score_zone(self, x: float, y: float):
        distance = math.sqrt(x**2 + y**2)

        for rayon, points in self.zones:
            if distance <= rayon:
                return points
        
        return 0

    def score_impact(self, x: float, y: float):
        return self.score_zone(x, y)

    def score_total(self):
        return sum(self.score_impact(x, y) for x, y in self.impacts)

    def afficher_impacts(self):
        print("=== Détail des impacts ===")
        if not self.impacts:
            print("Aucun impact enregistré.")
            return
        
        for i, (x, y) in enumerate(self.impacts, start=1):
            score = self.score_impact(x, y)
            print(f"Impact {i} : x={x:.1f} mm, y={y:.1f} mm -> score = {score}")

    def afficher_resume(self):
        print("=== Session de tir ===")
        print("Date :", self.date.strftime("%d/%m/%Y %H:%M"))
        print("Calibre :", self.calibre)
        print("Distance :", self.distance, "m")
        print("Nombre d'impacts :", self.nombre_impacts())
        print("Score total :", self.score_total())
