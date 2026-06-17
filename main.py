from analyse_ia import analyser_cible
from gestion_sessions import GestionSessions

def analyser_un_carton():
    print("=== Analyse d'un carton ===")

    # TODO : remplacer par un sélecteur de fichier dans ton interface
    chemin_image = "C:/Users/Alex/Desktop/ciblec50.jpg"

    # 1) Analyse IA → retourne une SessionTir
    session = analyser_cible(
        chemin_image,
        calibre="9mm",
        distance=25,
        nb_anneaux_theorique=10   # C50 par défaut
    )

    if session is None:
        print("Analyse impossible.")
        return

    # 2) Affichage console
    print("\n=== Résultat de l'analyse ===")
    session.afficher_resume()
    print()
    session.afficher_impacts()

    # 3) Ajout à l’historique (mais PAS progression)
    gestion = GestionSessions()
    gestion.ajouter_session(session)
    gestion.sauvegarder()

    print("\nLa séance a été analysée et enregistrée.")
    print("Elle pourra être envoyée vers la progression après validation.")

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Analyser un carton")
        print("2. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            analyser_un_carton()
        elif choix == "2":
            print("Fermeture de l'application.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
