# Code principal à ouvrir par l'utilisateur
##################### Variables ################
import os
# Décalage de l'encodage
cle = 0

# Text console à décoder // Fichier
texte_encode = []

# Texte console a encode //Fichier encodé


# brute force
texte_devine = []
cle_devine = []

# Input utilisateur


# Chemin
chemin_fichier = ''


#######################################
#########" Nom fonction "##############

def choix_de_la_fonction():
    print ("********************************************************************************* \n"
           "bonjour, ce code est un decripteur, il permet de cripter ou de decripter un texte \n"
           "********************************************************************************* \n \n")
    choix_fct = input(""
                      "Si vous voulez decripter, tapez 1, vous voulez cripter, tapez 2 : ,vous voulez decripter sans connaitre la clé, tapez 3 :")
    if choix_fct == str(1):
        print("vous avez choisi le decryptage")
        texte = get_texte_depuis_console_ou_fichier()
        if texte:
            cle = int(input("Tapez la clé ici svp : "))
            decode_cesar(texte, cle, True)
    if choix_fct == str(2):
        print("vous avez choisi le cryptage")
        encode_cesar()
    if choix_fct == str(3):
        print("vous avez choisi le brute force")
        brute_force_cesar()
    elif choix_fct != str(1) and choix_fct != str(2) and choix_fct != str(3):
        print("vous n'avez pas tape le bon charactere")

def entree_utilisateur_texte_seul():
    texte = input("Veuillez entrer le texte à déchiffrer : ")
    return texte

def entree_utilisateur():
    texte_cripte = str(input("pouvez vous indiquer ici votre texte  : "))
    entre_cle = input("tapez la cle ici svp : ")
    if entre_cle.strip() == "":
        return texte_cripte, None

    try:
        cle = int(entre_cle)
        return texte_cripte, cle
    except ValueError:
        print("La valeur entrée n'est pas un nombre valide.")
        return texte_cripte, None


def get_texte_depuis_console_ou_fichier():
    choix = input("Souhaitez-vous utiliser un fichier ou entrer le texte manuellement ? (fichier / texte) : ").lower()
    if choix == 'texte':
        texte = input("Veuillez entrer le texte ici : ")
        return texte
    elif choix == 'fichier':
        nom_fichier = input("Entrez le nom du fichier (avec .txt) : ")
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("Fichier non trouvé.")
            return None
    else:
        print("Choix invalide.")
        return None



def choix_du_fichier () :
    choix = str(input("Desirer vous effectuer le travail sur un fichier ou entrer le texte vous meme dans la console ? \n"
                      "ecrivez 'texte' pour entrez vous meme ou 'fichier' pour utiliser un fichier : "))
    if choix.lower() == 'texte':
        return 1
    elif choix.lower() == 'fichier':
        return 2
    else :
        print ("vous n'avez pas tape le bon charactere")



def encode_cesar():
    texte = get_texte_depuis_console_ou_fichier()
    if texte is None:
        return

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_code = ''
    cle = int(input("Tapez la clé ici svp : "))

    for lettre in texte:
        if lettre in alphabet:
            position = alphabet.index(lettre)
            nouvelle_position = (position + cle) % 26
            texte_code += alphabet[nouvelle_position]
        else:
            texte_code += lettre

    print('Voici le texte codé :', texte_code)
    with open("message_encrypte.txt", "w", encoding='utf-8') as f:
        f.write(texte_code)


def decode_cesar(text, decalage, booleen):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_decode = ''

    for lettre in text:
        if lettre in alphabet:
            position = alphabet.index(lettre)
            nouvelle_position = (position + decalage) % 26
            texte_decode += alphabet[nouvelle_position]
        else:
            texte_decode += lettre

    if booleen:
        print('Voici le texte décodé :', texte_decode)
    return texte_decode


def brute_force_cesar():
    texte = get_texte_depuis_console_ou_fichier()
    if texte is None:
        return

    meilleur_score = 0
    meilleure_decalage = 0
    texte_devine = ""

    for decalage in range(26):
        texte_decode = decode_cesar(texte, decalage, False)
        score = texte_decode.count('e')
        if score > meilleur_score:
            meilleur_score = score
            meilleure_decalage = decalage
            texte_devine = texte_decode

    print("Le texte deviné est :", texte_devine)
    print("Clé estimée :", meilleure_decalage)


def brute_force_cesar_manuel(text):
    while True:
        decalage = int(input("choisir le décalage: "))
        texte_decode = decode_cesar(text, decalage % 26, bool=False)
        print(texte_decode)
        retour_utilisateur = input("le resultat vous convient-il ? (o/n)")
        if retour_utilisateur.lower() == 'o':
            break
        else:
            print("Essayez un autre décalage.")

        # si oui on sort de la boucle


# text="yt h'peetaat vgddi"

# print(brute_force_cesar(text))

if __name__ == "__main__":
    choix_de_la_fonction()
    # encode_cesar()
    # decode_cesar()
    # brute_force_cesar()
    # brute_force_cesar_manuel()