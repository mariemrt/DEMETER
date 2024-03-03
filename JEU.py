# Taille de la grille
TAILLE_GRILLE = 8

# Constants pour représenter les pions et les buts
TAILLE_GRILLE = 8
PION_J1 = 'X'  # Pions du joueur 1
PION_J2 = 'O'  # Pions du joueur 2
BUT_J1 = 'B'  # But pour le Joueur 1
BUT_J2 = 'b'  # But pour le Joueur 2
VIDE = ' '  # Case vide

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
# Configuration "milieu" de la partie
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
    [VIDE, VIDE, VIDE, BUT_J2, BUT_J2, VIDE, VIDE, VIDE],
    [PION_J2, VIDE, PION_J2, VIDE, PION_J2, VIDE, PION_J2, VIDE],
    [VIDE, PION_J2, VIDE, PION_J2, VIDE, PION_J2, VIDE, PION_J2],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [PION_J1, VIDE, PION_J1, VIDE, PION_J1, VIDE, PION_J1, VIDE],
    [VIDE, PION_J1, VIDE, PION_J1, VIDE, PION_J1, VIDE, PION_J1],
    [VIDE, VIDE, VIDE, BUT_J1, BUT_J1, VIDE, VIDE, VIDE]
]


# Fonction pour afficher la grille
def afficher_grille(grille):
    # Affiche les en-têtes de colonne
    en_tetes_colonnes = '  ' + ' '.join('ABCDEFGH')  # Assurez-vous que cela correspond aux indices de votre grille
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


def est_dans_grille(ligne, colonne):
    # Vérifiez que l'indice de la ligne est compris entre 0 et TAILLE_GRILLE - 1
    # et que l'indice de la colonne est compris entre 0 et TAILLE_GRILLE - 1
    return 0 <= ligne < TAILLE_GRILLE and 0 <= colonne < TAILLE_GRILLE

def convertir_entree_en_indices(entree):
    # Convertir la lettre en indice de colonne (A=0, B=1, ...)
    # Convertir le chiffre en indice de ligne 0-based (1=0, 2=1, ...)
    colonne = ord(entree[0].upper()) - ord('A')
    ligne = int(entree[1]) - 1

    return ligne, colonne


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


def deplacement_a_domicile(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur):
    pion = PION_J1 if joueur == 1 else PION_J2

    # Vérifier si le déplacement est orthogonal et ne dépasse pas 7 cases
    deplacement_vertical = ligne_depart != ligne_arrivee and colonne_depart == colonne_arrivee
    deplacement_horizontal = ligne_depart == ligne_arrivee and colonne_depart != colonne_arrivee
    if not (deplacement_vertical or deplacement_horizontal):
        return False  # Déplacement invalide s'il n'est pas strictement horizontal ou vertical

    # Vérifier la distance du déplacement (doit être inférieure ou égale à 7)
    distance = max(abs(ligne_arrivee - ligne_depart), abs(colonne_arrivee - colonne_depart))
    if distance > 7:
        return False  # Déplacement invalide si la distance est supérieure à 7 cases

    # Vérifier que le pion se déplace dans son propre camp et ne traverse pas la ligne médiane
    ligne_mediane = TAILLE_GRILLE // 2
    if joueur == 1 and ligne_arrivee >= ligne_mediane:
        return False  # Déplacement invalide pour le joueur 1 si on traverse la ligne médiane
    if joueur == 2 and ligne_arrivee < ligne_mediane:
        return False  # Déplacement invalide pour le joueur 2 si on traverse la ligne médiane

    # Vérifier que le chemin est libre de tout autre pion
    # Pour un mouvement vertical
    if deplacement_vertical:
        direction = 1 if ligne_arrivee > ligne_depart else -1
        for i in range(ligne_depart + direction, ligne_arrivee, direction):
            if grille[i][colonne_depart] != VIDE:
                return False  # Le chemin n'est pas libre pour le déplacement

    # Pour un mouvement horizontal
    if deplacement_horizontal:
        direction = 1 if colonne_arrivee > colonne_depart else -1
        for i in range(colonne_depart + direction, colonne_arrivee, direction):
            if grille[ligne_depart][i] != VIDE:
                return False  # Le chemin n'est pas libre pour le déplacement
            # Finalement, effectuer le déplacement si toutes les vérifications sont passées
    grille[ligne_depart][colonne_depart], grille[ligne_arrivee][colonne_arrivee] = VIDE, pion
    return True


def deplacement_par_saut(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur):
    pion = PION_J1 if joueur == 1 else PION_J2
    # Calculer la position intermédiaire (celle du pion survolé)
    ligne_intermediaire = (ligne_depart + ligne_arrivee) // 2
    colonne_intermediaire = (colonne_depart + colonne_arrivee) // 2

    # Vérifier que le pion à la position de départ est bien celui du joueur actuel
    if grille[ligne_depart][colonne_depart] != pion:
        return False

    # Vérifier que le pion survolé est celui du joueur actuel
    if grille[ligne_intermediaire][colonne_intermediaire] != pion:
        return False

    # Vérifier que la case d'arrivée soit bien vide
    if grille[ligne_arrivee][colonne_arrivee] != VIDE:
        return False

    # Vérifier que le saut est en ligne droite (pas de mouvement en L)
    if ligne_depart != ligne_arrivee and colonne_depart != colonne_arrivee:
        dir_ligne = ligne_arrivee - ligne_depart
        dir_colonne = colonne_arrivee - colonne_depart
        # S'assurer que l'on saute sur un voisin direct
        if abs(dir_ligne) != 2 or abs(dir_colonne) != 2:
            return False
        # Effectuer le saut
    grille[ligne_depart][colonne_depart] = VIDE
    grille[ligne_arrivee][colonne_arrivee] = pion
    return True


def verifier_victoire(grille, joueur):
    pion = PION_J1 if joueur == 1 else PION_J2
    buts_adverses = [(0, 0), (0, 1)] if joueur == 2 else [(TAILLE_GRILLE - 1, TAILLE_GRILLE - 2),
                                                          (TAILLE_GRILLE - 1, TAILLE_GRILLE - 1)]

    # Vérifier la présence d'un pion dans les cases de but adverses
    for ligne, colonne in buts_adverses:
        if grille[ligne][colonne] == pion:
            return True  # Le joueur a gagné

    return False  # La victoire n'est pas encore déterminée

def valider_deplacement(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur):
    if grille[ligne_depart][colonne_depart] != (PION_J1 if joueur == 1 else PION_J2):
        return "Vous devez déplacer un de vos propres pions."

    if not est_dans_grille(ligne_arrivee, colonne_arrivee):
        return "La case de destination est hors de la grille."

    # Vérification si le mouvement est un déplacement à domicile ou par saut
    if abs(ligne_depart - ligne_arrivee) <= 7 and abs(colonne_depart - colonne_arrivee) <= 7:
        # Il s'agit d'un déplacement à domicile, car ni les lignes ni les colonnes ne changent de plus de 7
        if grille[ligne_arrivee][colonne_arrivee] != VIDE or grille[ligne_depart][colonne_depart] == VIDE:
            return "Déplacement à domicile impossible: soit la case de départ est vide, soit la destination n'est pas vide."
        else:
            return deplacement_a_domicile(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur)
    else:
        # Il s'agit d'un déplacement par saut.
        # On vérifie d'abord si la case de départ et la case d'arrivée forment une ligne droite valide pour le saut
        saut_valide = (
                ligne_depart != ligne_arrivee and colonne_depart != colonne_arrivee and
                abs((ligne_arrivee - ligne_depart) / (colonne_arrivee - colonne_depart)) == 1
        )
        if not saut_valide:
            return "Déplacement par saut impossible: le mouvement doit être en ligne droite."
        # Sauter par-dessus un pion sans franchir de cases
        milieu_ligne, milieu_colonne = (ligne_depart + ligne_arrivee) // 2, (colonne_depart + colonne_arrivee) // 2
        if grille[milieu_ligne][milieu_colonne] != (PION_J1 if joueur == 1 else PION_J2) or grille[ligne_arrivee][
            colonne_arrivee] != VIDE:
            return "Déplacement par saut impossible: vous devez sauter par-dessus un de vos propres pions sur une case adjacente dans une trajectoire linéaire et atterrir sur une case vide."
        else:
            return deplacement_par_saut(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur)

    # Si aucune des conditions ci-dessus n'est remplie, le déplacement est considéré comme non valide.
    return "Déplacement non valide selon les règles du jeu."


def traiter_tour(grille, joueur):
    # Le joueur indique où il souhaite déplacer son pion
    print(f"Tour du joueur {joueur}.")
    deplacement_validé = False
    while not deplacement_validé:
        entree_depart = input("Entrez les coordonnées du pion à déplacer (par ex. 'A1'): ")
        entree_arrivee = input("Entrez les coordonnées de destination (par ex. 'B2'): ")

        if not est_au_bon_format(entree_depart) or not est_au_bon_format(entree_arrivee):
            print("Entrées non valides, veuillez utiliser le format de coordonnées correct. Exemple: 'A3'.")
            continue

        ligne_depart, colonne_depart = convertir_entree_en_indices(entree_depart)
        ligne_arrivee, colonne_arrivee = convertir_entree_en_indices(entree_arrivee)

        if not est_dans_grille(ligne_depart, colonne_depart) or not est_dans_grille(ligne_arrivee, colonne_arrivee):
            print("Au moins l'une des coordonnées est en dehors de la grille. Veuillez entrer des coordonnées valides.")
            continue
        validation = valider_deplacement(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, joueur)

        if isinstance(validation, str):  # Si le retour est une chaîne, c'est un message d'erreur
            print(validation)
        else:
            deplacement_validé = validation


def demarrer_jeu(grille):
    joueur_actuel = 1  # Commence par le joueur 1
    while True:
        # Affiche la grille actuelle
        afficher_grille(grille)

        # Traite le tour du joueur actuel
        traiter_tour(grille, joueur_actuel)

        # Vérifie si le joueur actuel a gagné
        if verifier_victoire(grille, joueur_actuel):
            print(f"Félicitations, le joueur {joueur_actuel} a gagné la partie!")
            afficher_grille(grille)
            break  # Termine la boucle de jeu si un joueur a gagné

        # Change de joueur pour le prochain tour
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


if __name__ == "__main__":
    # Démarrez avec la grille de départ
    grille_actuelle = [ligne[:] for ligne in grille_depart]
    test_est_au_bon_format()
    test_est_dans_grille()
    # Lancer le jeu
    demarrer_jeu(grille_actuelle)


