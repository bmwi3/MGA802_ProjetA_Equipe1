#Code principal à ouvrir par l'utilisateur

import os

##################### Variables ################

# Décalage de l'encodage
cle=0

#Text console à décoder // Fichier
texte_encode=[]

#Texte console a encode //Fichier encodé


#brute force
texte_devine=[]
cle_devine=[]

#Input utilisateur


#Chemin
chemin_fichier=''

#######################################
#########" Nom fonction "##############
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def choix_de_la_fonction():
    choix_fct = input("bonjour, ce code est un decripteur, il permet de cripter ou de decripter un texte,\n"
          "Si vous voulez decripter, tapez 1, vous voulez cripter, tapez 2 : ,vous voulez decripter sans connaitre la clé, tapez 3 :")
    if choix_fct == str(1):
        texte, cle = entree_utilisateur()
        decode_cesar(texte, cle, True)  # Ajout de l'argument booleen ici
    if choix_fct == str(2):
        encode_cesar()
    if choix_fct == str(3):
        texte, _ = entree_utilisateur()  # On ignore la clé pour le brute force
        brute_force_cesar(texte)
    elif choix_fct != str(1) and choix_fct != str(2) and choix_fct != str(3):
        print("vous n'avez pas tape le bon charactere")


def entree_utilisateur():
    texte_cripte = str(input("pouvez vous indiquer ici votre texte  : "))
    entre_cle = input("tapez la cle ici svp : ")
    if entre_cle.strip() == "":
        return texte_cripte, None
    else:
        cle = int(entre_cle)
        return texte_cripte, cle
    

def encode_cesar(text, cle):
    texte_code = ''
    for lettre in text:
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

def decode_cesar(text, cle):
    # Pour déchiffrer, on inverse le décalage
    return encode_cesar(text, -cle)


# def decode_cesar(text,decalage,booleen):
    
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     texte_decode = ''

#     # if text == None and decalage == None:
#     #     print ("vous avez choisi le decrytage.")
#     #     text = str(input("pouvez vous indiquer ici le texte a decripter svp : "))
#     #     decalage = int(input("conaissez vous la cle, si oui, tapez la, sinon, tapez 0 : "))
   


#     for lettre in text :
#         if lettre in alphabet :
#             position = alphabet.index(lettre)
#             nouvelle_position = (position + decalage)%26
#             texte_decode += alphabet[nouvelle_position]
#         else :
#             texte_decode += lettre
#     if booleen == True:
#         print ('voici le texte decode : ', texte_decode)
#         return texte_decode
#     elif booleen == False:
#         return texte_decode
    





def brute_force_cesar(text):
    texte_devine = ""
    meilleur_score = 0
    meilleure_decalage = 0
    double=0
    for decalage in range(26):
        texte_decode = decode_cesar(text, decalage)
        #Nous sommes dans la langue francaise la lettre la plus fréquente est le E
        #On compte le nombre de E dans le texte décodé
        score = sum(1 for char in texte_decode if char=='e')
        #print(score)
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
    while True:
        decalage = int(input("choisir le décalage: "))
        texte_decode = decode_cesar(text, decalage)
        print(texte_decode)
        retour_utilisateur = input("le resultat vous convient-il ? (o/n)")
        if retour_utilisateur.lower() == 'o':
            break
        else:
            print("Essayez un autre décalage.")
        
        #si oui on sort de la boucle


#text="yt h'peetaat vgddi"

#print(brute_force_cesar(text))

def ouvrir_fichier():
    """Ouvre le fichier de mots et retourne une liste de mots.

    Returns:
        list: Liste des mots lus dans le fichier, ou False si le fichier n'est pas trouvé.
    """
    nom = input("Nom du fichier à lire : ")
    if not os.path.isfile(nom):
        print("Erreur : fichier introuvable.")
        return None, None
    with open(nom, encoding="utf-8") as f:
        texte = f.read()
    cle_entree = input("Veuillez entrer la clé (nombre entier, positif ou négatif) : ")
    if cle_entree is None or cle_entree.strip() == "":
        print("Erreur : la clé doit être un nombre entier.")
        return texte, None
    else:
        cle = int(cle_entree)
        return texte, cle

def sauvegarder_fichier(texte):
    nom = input("Nom du fichier pour sauvegarder le résultat : ")
    #w pour overwrite le fichier si il existe déjà
    with open(nom, "w", encoding="utf-8") as f:
        f.write(texte)
#source https://www.w3schools.com/python/python_file_write.asp

def main():
    print("Bonjour, ce code est un descripteur, il permet de cripter ou de descripter un texte,\n")
    #boucle infinie pour ne pas stopper le code
    while True:
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
                res = encode_cesar(texte, cle)
                print("\nTexte crypté :\n", res)
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
                res = encode_cesar(texte, cle)
                sauvegarder_fichier(res)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        elif choix_fct == "4":
            texte, cle = ouvrir_fichier()
            if texte is not None and cle is not None:
                res = decode_cesar(texte, cle)
                sauvegarder_fichier(res)
            else:
                print("Erreur : la clé doit être un nombre entier.")
                continue
        elif choix_fct == "5":
            texte = input("Veuillez entrer le texte à déchiffrer : ")
            brute_force_cesar(texte)
        elif choix_fct == "6":
            texte = ouvrir_fichier()
            brute_force_cesar(texte)
        else:
            print("Merci d'entrer un nombre entre 0 et 6.")
            break


if __name__ == "__main__":
    main()
    #encode_cesar()
    #decode_cesar()
    #brute_force_cesar()
    #brute_force_cesar_manuel()