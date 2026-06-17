import json
from session_tir import SessionTir

class GestionSessions:
    def __init__(self):
        self.sessions = []

    def ajouter_session(self, session: SessionTir):
        self.sessions.append(session)

    def afficher_historique(self):
        print("=== Historique des sessions ===")
        if not self.sessions:
            print("Aucune session enregistrée.")
            return
        
        for i, session in enumerate(self.sessions, start=1):
            print(f"Session {i} : {session.date.strftime('%d/%m/%Y %H:%M')} - {session.calibre} - {session.distance}m - Score {session.score_total()}")

    def sauvegarder(self, fichier="sessions.json"):
        data = []
        for s in self.sessions:
            data.append({
                "date": s.date.strftime("%Y-%m-%d %H:%M:%S"),
                "calibre": s.calibre,
                "distance": s.distance,
                "impacts": s.impacts,
                "zones": s.zones
            })

        with open(fichier, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Sessions sauvegardées dans {fichier}")

    def charger(self, fichier="sessions.json"):
        try:
            with open(fichier, "r") as f:
                data = json.load(f)

            self.sessions = []
            for s in data:
                session = SessionTir(
                    calibre=s["calibre"],
                    distance=s["distance"],
                    zones=s["zones"]
                )
                for x, y in s["impacts"]:
                    session.ajouter_impact(x, y)
                self.sessions.append(session)

            print(f"{len(self.sessions)} sessions chargées depuis {fichier}")

        except FileNotFoundError:
            print("Aucun fichier de sessions trouvé.")
