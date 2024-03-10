# Taille de la grille
TAILLE_GRILLE = 8

# Constants pour représenter les pions et les buts
PION_J1 = 'X' # Pions du joueur 1
PION_J2 = 'O' # Pions du joueur 2
BUT_J1 = 'B' # But pour le Joueur 1
BUT_J2 = 'b' # But pour le Joueur 2
VIDE = ' ' # Case vide


# Initialisation de la grille au début du jeu
grille_depart = [
    [VIDE, VIDE, VIDE, BUT_J2, BUT_J2, VIDE, VIDE, VIDE],
    [PION_J2, VIDE, PION_J2, VIDE, PION_J2, VIDE, PION_J2, VIDE],
    [VIDE, PION_J2, VIDE, PION_J2, VIDE, PION_J2, VIDE, PION_J2],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [PION_J1, VIDE, PION_J1, VIDE, PION_J1, VIDE, PION_J1, VIDE],
    [VIDE, PION_J1, VIDE, PION_J1, VIDE, PION_J1, VIDE, PION_J1],
    [VIDE, VIDE, VIDE, BUT_J1, BUT_J1, VIDE, VIDE, VIDE]
]
# Configuration "milieu" de la partie1
grille_milieu = [
    [PION_J2, VIDE, VIDE, BUT_J2, BUT_J2, VIDE, VIDE, PION_J2],
    [VIDE, VIDE, VIDE, PION_J2, VIDE, VIDE, PION_J2, VIDE],
    [VIDE, PION_J2, VIDE, VIDE, VIDE, VIDE, VIDE, PION_J2],
    [VIDE, VIDE, VIDE, PION_J2, VIDE, PION_J2, VIDE, VIDE],
    [VIDE, PION_J1, VIDE, VIDE, VIDE, VIDE, VIDE, PION_J1],
    [VIDE, PION_J1, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [PION_J1, VIDE, PION_J1, VIDE, VIDE, PION_J1, VIDE, VIDE],
    [VIDE, PION_J1, VIDE, BUT_J1, BUT_J1, VIDE, VIDE, PION_J1]
]

# Configuration "fin" de la partie (quelques coups avant la fin)
grille_fin = [
    [PION_J2, VIDE, PION_J1, BUT_J2, BUT_J2, VIDE, VIDE, PION_J1],
    [VIDE, PION_J1, VIDE, VIDE, VIDE, VIDE, PION_J1, VIDE],
    [VIDE, VIDE, PION_J1, VIDE, PION_J1, VIDE, VIDE, PION_J2],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, PION_J2, VIDE],
    [VIDE, PION_J1, VIDE, PION_J2, VIDE, PION_J2, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, PION_J1, PION_J2],
    [VIDE, PION_J2, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, BUT_J1, BUT_J1, VIDE, PION_J2, VIDE]
]


# Fonction pour afficher la grille
def afficher_grille(grille):
    # Affiche les en-têtes de colonne
    en_tetes_colonnes = '  ' + ' '.join(' A B C D E F G H')
    print(en_tetes_colonnes)

    # Affichage de la ligne de séparation
    ligne_separation = '+' + '---+' * TAILLE_GRILLE
    print(ligne_separation)

    # Affichage des lignes de la grille avec les numéros de ligne
    for i, ligne in enumerate(grille):
        # Convertir la ligne en chaîne de caractères, en joignant les éléments par des espaces
        contenu_ligne = '| ' + ' | '.join(ligne) + ' |'
        print(f"{i + 1} {contenu_ligne}")  # Ajoutez le numéro de la ligne à gauche
        print(ligne_separation)


# Fonction pour vérifier si l'entrée est au bon format
def est_au_bon_format(entree):
    # Assurer que l'entrée a une longueur de deux caractères
    if len(entree) != 2:
        return False

    lettre_colonne, chiffre_ligne = entree[0], entree[1]

    # Vérifier si la première partie de l'entrée est bien une lettre entre A et H
    if not lettre_colonne.upper() in 'ABCDEFGH':
        return False

    # Vérifier si la deuxième partie de l'entrée est bien un chiffre entre 1 et 8
    if not chiffre_ligne.isdigit() or not 1 <= int(chiffre_ligne) <= 8:
        return False

    # Les deux conditions sont vraies, l'entrée est au bon format
    return True

# Fonction pour vérifier si les indices sont dans la grille
def est_dans_grille(ligne, colonne):
    # Vérifiez que l'indice de la ligne est compris entre 0 et TAILLE_GRILLE - 1
    # et que l'indice de la colonne est compris entre 0 et TAILLE_GRILLE - 1
    return 0 <= ligne < TAILLE_GRILLE and 0 <= colonne < TAILLE_GRILLE

# Fonction pour convertir l'entrée en indices de grille
def convertir_entree_en_indices(entree):
    # Convertir la lettre en indice de colonne (A=0, B=1, ...)
    # Convertir le chiffre en indice de ligne 0-based (1=0, 2=1, ...)
    colonne = ord(entree[0].upper()) - ord('A')
    ligne = int(entree[1]) - 1
    return ligne, colonne

# Fonction pour saisir les coordonnées
def saisir_coordonnees():
    while True:
        entree = input("Entrez les coordonnées (par ex. 'A1'): ")

        # Vérifier le format de l'entrée
        if not est_au_bon_format(entree):
            print("Format non valide. Veuillez entrer la lettre suivie du numéro (exemple: 'A1').")
            continue

        # Convertir l'entrée en indices de grille
        ligne, colonne = convertir_entree_en_indices(entree)

        # Vérifier si les indices sont dans la grille
        if not est_dans_grille(ligne, colonne):
            print("Les coordonnées sont hors de la grille. Veuillez entrer des coordonnées valides.")
            continue

        # Si l'entrée est correcte et dans la grille, retourner les coordonnées
        return ligne, colonne
    

# Fonction pour valider le déplacement à domicile
def valider_deplacement_a_domicile(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur):
    pion = PION_J1 if joueur == 1 else PION_J2

    # Vérifier si la case de départ contient le pion du joueur actuel
    if grille[ligne_depart][colonne_depart] != pion:
        return "La case de départ ne contient pas votre pion."

    # Vérification si le mouvement est un déplacement à domicile
    distance_ligne = abs(ligne_depart - ligne_arrivee)
    distance_colonne = abs(colonne_depart - colonne_arrivee)

    if distance_ligne <= 7 and distance_colonne <= 7:
        # Vérifier si le déplacement ne dépasse pas la ligne médiane
        if joueur == 1 and ligne_arrivee <= 3:
            return "Déplacement à domicile impossible au-delà de la ligne médiane."
        elif joueur == 2 and ligne_arrivee >= 4:
            return "Déplacement à domicile impossible au-delà de la ligne médiane."
        
        # Vérifier si la case de départ n'est pas vide
        if grille[ligne_depart][colonne_depart] == VIDE:
            return "La case de départ est vide."

        # Vérifier qu'aucun pion n'est sauté pendant le déplacement
        if distance_ligne == 0 and distance_colonne > 1:
            for col in range(min(colonne_depart, colonne_arrivee) + 1, max(colonne_depart, colonne_arrivee)):
                if grille[ligne_arrivee][col] != VIDE:
                    return "Déplacement à domicile impossible. Un pion est sauté."

        elif distance_colonne == 0 and distance_ligne > 1:
            for row in range(min(ligne_depart, ligne_arrivee) + 1, max(ligne_depart, ligne_arrivee)):
                if grille[row][colonne_arrivee] != VIDE:
                    return "Déplacement à domicile impossible. Un pion est sauté."

        # Il s'agit d'un déplacement à domicile
        if grille[ligne_arrivee][colonne_arrivee] == VIDE:
            grille[ligne_depart][colonne_depart], grille[ligne_arrivee][colonne_arrivee] = VIDE, pion
            return None  # Le déplacement à domicile est valide
        else:
            return "La case de destination est déjà occupée."

    return "Le mouvement n'est pas un déplacement à domicile."


def valider_deplacement_par_saut(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur):
    pion = PION_J1 if joueur == 1 else PION_J2

    # Vérifier que le pion à la position de départ est bien celui du joueur actuel
    if grille[ligne_depart][colonne_depart] != pion:
        return False

    # Vérifier que la case d'arrivée soit bien vide
    if grille[ligne_arrivee][colonne_arrivee] != VIDE:
        return False

    while True:
        # Calculer la position intermédiaire (celle du pion survolé)
        ligne_intermediaire = (ligne_depart + ligne_arrivee) // 2
        colonne_intermediaire = (colonne_depart + colonne_arrivee) // 2

        # Vérifier que le saut est en ligne droite (pas de mouvement en L)
        if ligne_depart != ligne_arrivee and colonne_depart != colonne_arrivee:
            dir_ligne = ligne_arrivee - ligne_depart
            dir_colonne = colonne_arrivee - colonne_depart
            # S'assurer que l'on saute sur un voisin direct
            if abs(dir_ligne) != 2 or abs(dir_colonne) != 2:
                return False

        # Vérifier que l'on saute par-dessus un de ses propres pions
        if grille[ligne_intermediaire][colonne_intermediaire] != pion:
            return False

        # Effectuer le saut
        grille[ligne_depart][colonne_depart] = VIDE
        grille[ligne_arrivee][colonne_arrivee] = pion

        # Afficher la grille après le saut
        afficher_grille(grille)

        # Demander au joueur s'il veut effectuer un autre saut
        continuer_saut = input("Voulez-vous effectuer un autre saut? (Oui/Non): ").lower()
        if continuer_saut != 'oui':
            break

        # Si le joueur souhaite continuer, saisir de nouvelles coordonnées d'arrivée
        nouvelle_arrivee = saisir_coordonnees()
        ligne_depart, colonne_depart = ligne_arrivee, colonne_arrivee
        ligne_arrivee, colonne_arrivee = nouvelle_arrivee

    return True




def demander_type_deplacement():
    while True:
        type_deplacement = input("Voulez-vous effectuer un déplacement à domicile ou un saut? (d/s): ").lower()
        if type_deplacement in ['d', 's']:
            return type_deplacement
        else:
            print("Veuillez entrer 'd' pour un déplacement à domicile ou 's' pour un saut.")



# Fonction principale du jeu
def jouer():
    print("Bienvenue")

    # Demander à l'utilisateur de choisir la configuration de départ
    choix = input("Choisissez la configuration de départ (1: Début, 2: Milieu, 3: Fin): ")
    if choix == '1':
        grille = grille_depart
    elif choix == '2':
        grille = grille_milieu
    elif choix == '3':
        grille = grille_fin
    else:
        print("Choix invalide. Configuration de départ par défaut.")
        grille = grille_depart

    joueur_actuel = 1

    while True:
        # Afficher la grille actuelle
        afficher_grille(grille)

        print(f"C'est au tour du joueur {joueur_actuel}.")

        # Demander au joueur le type de déplacement
        type_deplacement = demander_type_deplacement()

        # Saisir les coordonnées du pion à déplacer
        print("Saisissez les coordonnées du pion à déplacer:")
        ligne_depart, colonne_depart = saisir_coordonnees()

        # Saisir les coordonnées de la case de destination
        print("Saisissez les coordonnées de la case de destination:")
        ligne_arrivee, colonne_arrivee = saisir_coordonnees()

        # Valider le déplacement en fonction du type choisi
        if type_deplacement == 'd':
            erreur = valider_deplacement_a_domicile(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur_actuel)
        elif type_deplacement == 's':
            erreur = valider_deplacement_par_saut(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur_actuel)
        else:
            print("Type de déplacement invalide. Veuillez choisir 'd' pour un déplacement à domicile ou 's' pour un saut.")
            continue

        if erreur is not None:
            print(f"Erreur : {erreur}")
            continue

        # Afficher la grille après le déplacement
        afficher_grille(grille)

        # Passer au joueur suivant
        joueur_actuel = 2 if joueur_actuel == 1 else 1

# Tests pour la fonction est_au_bon_format
def test_est_au_bon_format():
    assert est_au_bon_format("A1"), "A1 devrait être un format valide"
    assert est_au_bon_format("H8"), "H8 devrait être un format valide"
    assert not est_au_bon_format("A0"), "A0 devrait être un format invalide (numéro invalide)"
    assert not est_au_bon_format("I1"), "I1 devrait être un format invalide (lettre invalide)"
    assert not est_au_bon_format("11"), "11 devrait être un format invalide (manque de lettre)"
    print("test_est_au_bon_format: tous les tests passent")

# Tests pour la fonction est_dans_grille
def test_est_dans_grille():
    assert est_dans_grille(0, 0), "(0,0) devrait être dans la grille"
    assert est_dans_grille(7, 7), "(7,7) devrait être dans la grille"
    assert not est_dans_grille(-1, 0), "(-1,0) ne devrait pas être dans la grille (ligne invalide)"
    assert not est_dans_grille(0, 8), "(0,8) ne devrait pas être dans la grille (colonne invalide)"
    print("test_est_dans_grille: tous les tests passent")


# Lancer le jeu
jouer()