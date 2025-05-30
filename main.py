################# Ce code permet de réaliser du criptage decriptage de césar ##################
# Il est constitué de différentes fonctions chacun réalisant une opérations particulière
# Le code va afficher un menu permettant à l'utilisateur de sélectionner la fonctionnalité qu'il veut

######### Importation des bibliothèques nécessaires #######
import os
import unicodedata
from time import perf_counter
########## Variable globale ##############
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

############# Fonctions ##############
def enlever_caracteres_speciaux(mot):
    """Enlève les caractères spéciaux d'un texte.

    Args:
        mot (str): Le texte à normaliser.

    Returns:
        str: Le texte normalisé sans caractères spéciaux.
    """
    mot_normalise = unicodedata.normalize('NFKD', mot)
    return ''.join([char.lower() for char in mot_normalise 
                if (char.isalpha() or char == " ") and not unicodedata.combining(char)]
    )

def entree_utilisateur():
    """Demande le texte à chiffrer et déchiffrer ainsi que la clé.
    Normalise le texte.

    Returns:
        texte_normalise (str): texte qui va être encoder/décoder par la suite.
        cle (int): clé de chiffrement/dechiffrement ou None si aucune clé n'est entrée.
    """
    texte_cripte = str(input("pouvez vous indiquer ici votre texte  : "))
    texte_normalise = enlever_caracteres_speciaux(texte_cripte)
    entre_cle = input("tapez la cle ici svp : ")
    #Si l'utilisateur n'entre pas de clé, on retourne le texte normalisé et None
    if entre_cle.strip() == "":
        return texte_normalise, None
    else:
        cle = int(entre_cle)
        return texte_normalise, cle
    

def encode_cesar(texte, cle):
    """Réalise l'encodage du texte.

    Args:
        texte (str): Le texte à encoder.
        cle (int): La clé de chiffrement.

    Returns:
        texte_code (str): Le texte encodé/decodé.
    """
    texte_code = ''
    # On parcourt chaque lettre du texte
    for lettre in texte:
        # On vérifie si la lettre est dans l'alphabet
        # Si oui, on calcule sa position dans l'alphabet
        # On applique le décalage et on récupère la nouvelle lettre
        # Modulo 26 pour rester dans les limites de l'alphabet
        if lettre.lower() in ALPHABET:
            position = ALPHABET.index(lettre.lower())
            nouvelle_position = (position + cle) % 26
            nouvelle_lettre = ALPHABET[nouvelle_position]
            if lettre.isupper():
                nouvelle_lettre = nouvelle_lettre.upper()
            texte_code += nouvelle_lettre
        else:
            texte_code += lettre
    return texte_code

def decode_cesar(texte, cle):
    """Réalise le decodage du texte en utilisant la fonction encodage.
        Déchiffrer revient à encoder avec un décalage négatif ou à inverser le décalage.

    Args:
        texte (str): Le texte à décoder.
        cle (int): La clé de chiffrement.

    Returns:
        texte_code (str): Le texte decodé.
    """
    # Si la clé est negative son inverse est positif et vice versa
    return encode_cesar(texte, -cle)

#méthode vu sur https://www.dcode.fr/chiffre-cesar

def brute_force_cesar(texte):
    """Réalise le decodage du texte sans connaitre la clé.
    Nous sommes dans la langue francaise la lettre la plus fréquente est le E
    On compte le nombre de E dans le texte décodé
    Cette méthode est plus fiable avec un texte long.

    Args:
        texte (str): Le texte qui est à décoder.

    Returns:
        texte_devine (str): Le texte qui est la solution la plus probable.
        meilleur_score (int): Le score du texte deviné, basé sur la fréquence de la lettre 'e'.
        meilleure_decalage (int): Le décalage utilisé pour obtenir le texte deviné.
    """
    texte_devine = ""
    meilleur_score = 0
    meilleure_decalage = 0
    # On essaie tous les décalages de 0 à 26
    tic=perf_counter()
    for decalage in range(27):
        texte_decode = decode_cesar(texte, decalage)
        # On compte le nombre de 'e' dans le texte décodé
        score = sum(1 for char in texte_decode if char=='e')
        # Si le score est meilleur que le meilleur score précédent, on met à jour
        if score > meilleur_score:
            meilleur_score = score
            texte_devine = texte_decode
            meilleure_decalage = decalage
    toc=perf_counter()
    print("Temps d'exécution pour la brute force : ", toc-tic, "secondes")
    print("le texte devine est : ", texte_devine)
    # On demande à l'utilisateur s'il est satisfait du résultat sinon on passe en mode brute force manuel
    satisfait = input("Êtes-vous satisfait du résultat ? (o/n) : ")
    if satisfait.lower() != 'o':
        print("Passage en mode brute force manuel.")
        brute_force_cesar_manuel(texte)
    return texte_devine, meilleure_decalage, meilleur_score


def brute_force_cesar_manuel(texte):
    """Réalise le decodage du texte sans connaitre la clé.
    Demande à l'utilisateur à chaque itération une clé jusqu'a ce que l'utilisateur soit satisfait.
    Méthode plus interactive mais pas forcement efficiente.

    Args:
        texte (str): Le texte qui est à décoder.

    Returns:
        texte_devine (str): Le texte qui est la solution la plus probable.
        meilleur_score (int): Le score du texte deviné, basé sur la fréquence de la lettre 'e'.
        meilleure_decalage (int): Le décalage utilisé pour obtenir le texte deviné.
    """
    while True:
        decalage = int(input("choisir le décalage: "))
        texte_decode = decode_cesar(texte, decalage)
        print(texte_decode)
        retour_utilisateur = input("le resultat vous convient-il ? (o/n)")
        #si oui on sort de la boucle
        if retour_utilisateur.lower() == 'o':
            break
        else:
            print("Essayez un autre décalage.")
    return texte_decode


def ouvrir_fichier():
    """Ouvre le fichier de mots et retourne une liste de mots.

    Returns:
        texte (str): Liste des mots lus dans le fichier, ou False si le fichier n'est pas trouvé.
        clé (int): Clé de chiffrement/dechiffrement ou None si aucune clé n'est entrée.
    """
    nom = input("Nom du fichier à lire (attention selon le nom du document il faut parfois mettre .txt): ")
    # On vérifie si le fichier existe
    if not os.path.isfile(nom):
        print("Erreur : fichier introuvable.")
        return None, None
    # On ouvre le fichier en mode lecture
    with open(nom,'r', encoding="utf-8") as f:
        texte = f.read()
    cle_entree = input("Veuillez entrer la clé (nombre entier, positif ou négatif) : ")
    # Si l'utilisateur n'entre pas de clé, on retourne le texte et None
    # Sinon on cast la clé en entier
    if cle_entree is None or cle_entree.strip() == "":
        print("Vous n'avez pas entré de clé.")
        return texte, None
    else:
        cle = int(cle_entree)
        return texte, cle

def sauvegarder_fichier(texte):
    """Enregistre le fichier de mots après l'opération effectué.
    """
    nom = input("Nom du fichier pour sauvegarder le résultat : ")
    #w pour overwrite le fichier si il existe déjà
    with open(nom, "w", encoding="utf-8") as f:
        f.write(texte)
    print("Sauvegarde réussie\n")
#source https://www.w3schools.com/python/python_file_write.asp


def brute_force_dictionnaire(texte):
    """Réalise le decodage du texte sans connaitre la clé.
    Utilise un dictionnaire de mots français pour trouver le mot le plus probable.

    Args:
        texte (str): Le texte qui est à décoder.

    Returns:
        texte_devine (str): Le texte qui est la solution la plus probable.
        decalage (int): Le décalage trouvé.
    """
    texte_devine = ""
    if not os.path.isfile("liste_francais.txt"):
        print("Erreur : fichier 'liste_francais.txt' introuvable.")
        return None, None
    else:
        with open("liste_francais.txt", "r") as f:
            dictionnaire = f.read().splitlines()
        # On enlève les caractères spéciaux du mot chiffré
        texte_formate = enlever_caracteres_speciaux(texte)
        liste_texte = texte_formate.split()
        dictionnaire = [enlever_caracteres_speciaux(mot) for mot in dictionnaire]
        mot_1 = liste_texte[0]


    # Analyse performance
    tic=perf_counter()
    # On essaie tous les décalages de 0 à 26
    for decalage in range(27):
        mot_1_decode = decode_cesar(mot_1, decalage)
        # On vérifie si le mot déchiffré est dans le dictionnaire
        # On ignore les mots de moins de 3 lettres
        if mot_1_decode in dictionnaire and len(mot_1_decode) > 2:  
            texte_devine = decode_cesar(texte, decalage)
            break
        # Si le mot déchiffré est dans le dictionnaire mais de moins de 3 lettres
        # On vérifie le mot suivant dans la liste
        elif mot_1_decode in dictionnaire and len(mot_1_decode) <= 2:
            mot_2=liste_texte[1]
            i=1
            while len(mot_2) < 2 and i < len(liste_texte)-1:
                i=i+1
                mot_2=liste_texte[i]
            
            mot_2_decode = decode_cesar(mot_2, decalage)
            
            if mot_2_decode in dictionnaire:
                
                texte_devine = decode_cesar(texte, decalage)
                break       
    toc=perf_counter()
    print("Temps d'exécution pour la brute force : ", toc-tic, "secondes")
    print("le texte devine est : ", texte_devine)
    return texte_devine,decalage




def main():
    """Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    Demande à l'utilisateur de choisir une option et appelle la fonction correspondante.
    """
    # Affichage du message d'accueil au premier lancement
    print("\nBonjour, ce code est un decripteur, il permet de cripter ou de decripter un texte ou un fichier.")
    #boucle infinie pour ne pas stopper le code
    # Le code s'arrête si l'utilisateur entre un nombre autre que 1, 2, 3, 4, 5 ou 6
    while True:
        print("\nChoisir une option")
        print("1. Encoder un texte")
        print("2. Décoder un texte")
        print("3. Encoder un texte depuis un fichier")
        print("4. Décoder un texte depuis un fichier")
        print("5. Brute force basé sur la répétition de e sur un texte entré manuellement")
        print("6. Brute force basé sur la répétition de e sur un texte depuis un fichier")
        print("7. Brute force via reconnaissance d'un mot dans un dictionnaire sur un texte entré manuellement")
        print("8. Brute force via reconnaissance d'un mot dans un dictionnaire sur un texte depuis un fichier")
        choix_fct = input("Votre choix : ")
        #usage de if else if pour remplacer le switch case
        # Encoder le texte
        if choix_fct == "1":
            texte, cle = entree_utilisateur()
            if cle is not None:
                resultat = encode_cesar(texte, cle)
                print("\nTexte crypté :\n", resultat)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        # Décoder le texte
        elif choix_fct == "2":
            texte, cle = entree_utilisateur()
            if cle is not None:
                res = decode_cesar(texte, cle)
                print("\nTexte décrypté :\n", res)
            else:
                print("Erreur : la clé doit être un nombre entier.\n")
                print("Sans clé merci d'utiliser brute force.\n")
                continue
        # Encoder le texte depuis un fichier
        elif choix_fct == "3":
            texte, cle = ouvrir_fichier()
            if texte is not None and cle is not None:
                resultat = encode_cesar(texte, cle)
                sauvegarder_fichier(resultat)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        # Décoder le texte depuis un fichier
        elif choix_fct == "4":
            texte, cle = ouvrir_fichier()
            if texte is not None and cle is not None:
                resultat = decode_cesar(texte, cle)
                sauvegarder_fichier(resultat)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        # Brute force sur un texte entré manuellement
        elif choix_fct == "5":
            texte = input("Veuillez entrer le texte à déchiffrer : ")
            brute_force_cesar(texte)
        # Brute force sur un texte depuis un fichier
        elif choix_fct == "6":
            texte, cle = ouvrir_fichier()
            resultat,_ =brute_force_cesar(texte)
            sauvegarder_fichier(resultat)
        elif choix_fct == "7":
            texte = input("Veuillez entrer le texte à déchiffrer : ")
            if texte is not None:
                brute_force_dictionnaire(texte)
                
            else:
                print("Veillez entrer un texte valide.")
                continue
        elif choix_fct == "8":
            texte, cle = ouvrir_fichier()
            if texte is not None:
                resultat,_ = brute_force_dictionnaire(texte)
                sauvegarder_fichier(resultat)
            else:
                print("Erreur : le fichier n'a pas pu être ouvert.")
                continue
        else:
            print("Merci d'entrer un nombre entre 0 et 8.")
            break

############## Main ###############
if __name__ == "__main__":
    main()
