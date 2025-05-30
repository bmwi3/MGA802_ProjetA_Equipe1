################# Ce code permet de réaliser du criptage decriptage de césar ##################
# Il est constitué de différentes fonctions chacun réalisant une opérations particulière
# Le code va afficher un menu permettant à l'utilisateur de sélectionner la fonctionnalité qu'il veut

######### Importation des bibliothèques nécessaires #######
import os
import unicodedata

########## Variable globale ##############
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def enlever_caracteres_speciaux(mot):
    """Enlève les caractères spéciaux d'un texte.

    Args:
        mot (str): Le texte à normaliser.

    Returns:
        str: Le texte normalisé sans caractères spéciaux.
    """
    mot_normalise = unicodedata.normalize('NKFD', mot)
    return ''.join([char for char in mot_normalise if not unicodedata.combining(char)]
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
    for lettre in texte:
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
    for decalage in range(26):
        texte_decode = decode_cesar(texte, decalage)
        score = sum(1 for char in texte_decode if char=='e')

        if score > meilleur_score:
            meilleur_score = score
            texte_devine = texte_decode
            meilleure_decalage = decalage

    print("le texte devine est : ", texte_devine)
    satisfait = input("Êtes-vous satisfait du résultat ? (o/n) : ")
    if satisfait.lower() != 'o':
        print("Passage en mode brute force manuel.")
        brute_force_cesar_manuel(text)
    return texte_devine, meilleure_decalage, meilleur_score


def brute_force_cesar_manuel(text):
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
        texte_decode = decode_cesar(text, decalage)
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
    nom = input("Nom du fichier à lire : ")
    if not os.path.isfile(nom):
        print("Erreur : fichier introuvable.")
        return None, None
    with open(nom, encoding="utf-8") as f:
        texte = f.read()
    cle_entree = input("Veuillez entrer la clé (nombre entier, positif ou négatif) : ")
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

def main():
    """Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    Demande à l'utilisateur de choisir une option et appelle la fonction correspondante.
    """
    print("Bonjour, ce code est un decripteur, il permet de cripter ou de decripter un texte,\n")
    #boucle infinie pour ne pas stopper le code
    while True:
        print("Choisir une option")
        print("1. Encoder un texte")
        print("2. Décoder un texte")
        print("3. Encoder un texte depuis un fichier")
        print("4. Décoder un texte depuis un fichier")
        print("5. Brute force sur un texte entré manuellement")
        print("6. Brute force sur un texte depuis un fichier")
        choix_fct = input("Votre choix : ")
        #usage de if else if pour remplacer le switch case
        if choix_fct == "1":
            texte, cle = entree_utilisateur()
            if cle is not None:
                resultat = encode_cesar(texte, cle)
                print("\nTexte crypté :\n", resultat)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        elif choix_fct == "2":
            texte, cle = entree_utilisateur()
            if cle is not None:
                res = decode_cesar(texte, cle)
                print("\nTexte décrypté :\n", res)
            else:
                print("Erreur : la clé doit être un nombre entier.\n")
                print("Sans clé merci d'utiliser brute force.\n")
                continue
        elif choix_fct == "3":
            texte, cle = ouvrir_fichier()
            if texte is not None and cle is not None:
                resultat = encode_cesar(texte, cle)
                sauvegarder_fichier(resultat)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        elif choix_fct == "4":
            texte, cle = ouvrir_fichier()
            if texte is not None and cle is not None:
                resultat = decode_cesar(texte, cle)
                sauvegarder_fichier(resultat)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        elif choix_fct == "5":
            texte = input("Veuillez entrer le texte à déchiffrer : ")
            brute_force_cesar(texte)
        elif choix_fct == "6":
            texte, cle = ouvrir_fichier()
            brute_force_cesar(texte)
        else:
            print("Merci d'entrer un nombre entre 0 et 6.")
            break


if __name__ == "__main__":
    main()
