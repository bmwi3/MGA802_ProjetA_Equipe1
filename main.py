#Code principal à ouvrir par l'utilisateur
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

def choix_de_la_fonction():
    choix_fct = input("bonjour, ce code est un decripteur, il permet de cripter ou de decripter un texte,\n"
          "Si vous voulez decripter, tapez 1, vous voulez cripter, tapez 2 : ,vous voulez decripter sans connaitre la clé, tapez 3 :")
    if choix_fct == str(1):
        texte, cle = entree_utilisateur()
        decode_cesar(texte, cle)
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
    
    try:
        cle = int(entre_cle)
        return texte_cripte, cle
    except ValueError:
        print("La valeur entrée n'est pas un nombre valide.")
        return texte_cripte, None

def encode_cesar() :

    input("vous avez choisi le cryptage")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_cripte = str(input("pouvez vous indiquer ici le texte a cripter svp : "))
    cle = int(input("tapez la cle ici svp : "))
    texte_decode = ''

    for lettre in texte_cripte:
        if lettre in alphabet:
            position = alphabet.index(lettre)
            nouvelle_position = (position + cle) % 26
            texte_decode += alphabet[nouvelle_position]
        else:
            texte_decode += lettre

    print('voici le texte code : ', texte_decode)


def decode_cesar(text,decalage,booleen):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_decode = ''

    # if text == None and decalage == None:
    #     print ("vous avez choisi le decrytage.")
    #     text = str(input("pouvez vous indiquer ici le texte a decripter svp : "))
    #     decalage = int(input("conaissez vous la cle, si oui, tapez la, sinon, tapez 0 : "))
   


    for lettre in text :
        if lettre in alphabet :
            position = alphabet.index(lettre)
            nouvelle_position = (position + decalage)%26
            texte_decode += alphabet[nouvelle_position]
        else :
            texte_decode += lettre
    if booleen == True:
        print ('voici le texte decode : ', texte_decode)
        return texte_decode
    elif booleen == False:
        return texte_decode
    





def brute_force_cesar(text):
    texte_devine = ""
    meilleur_score = 0
    meilleure_decalage = 0
    double=0
    for decalage in range(26):
        texte_decode = decode_cesar(text, decalage,False)
        #Nous sommes dans la langue francaise la lettre la plus fréquente est le E
        #On compte le nombre de E dans le texte décodé
        score = sum(1 for char in texte_decode if char=='e')
        #print(score)
        if score > meilleur_score:
            meilleur_score = score
            texte_devine = texte_decode
            meilleure_decalage = decalage

    print("le texte devine est : ", texte_devine)
    return texte_devine, meilleure_decalage, meilleur_score


def brute_force_cesar_manuel(text):
    while True:
        decalage = int(input("choisir le décalage: "))
        texte_decode = decode_cesar(text, decalage%26, bool=False)
        print(texte_decode)
        retour_utilisateur = input("le resultat vous convient-il ? (o/n)")
        if retour_utilisateur.lower() == 'o':
            break
        else:
            print("Essayez un autre décalage.")
        
        #si oui on sort de la boucle


#text="yt h'peetaat vgddi"

#print(brute_force_cesar(text))

if __name__ == "__main__":
    choix_de_la_fonction()
    #encode_cesar()
    #decode_cesar()
    #brute_force_cesar()
    #brute_force_cesar_manuel()