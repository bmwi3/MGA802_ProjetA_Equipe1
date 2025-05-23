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

def choix_de_la_fonction () :
    choix_fct = (input("bonjour, ce code est un decripteur, il permet de cripter ou de decripter un texte," '\n'
          "Si vous voulez decripter, tapez 1, sinon, tapez 2 : "))
    if choix_fct == str(1) :
        decode_cesar()
    if choix_fct == str(2) :
        encode_cesar()
    elif choix_fct != str(1) and choix_fct != str(2) :
        print("vous n'avez pas tape le bon charactere")


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


def decode_cesar() :

    print ("vous avez choisi le decrytage.")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_cripte = str(input("pouvez vous indiquer ici le texte a decripter svp : "))
    cle = int(input("conaissez vous la cle, si oui, tapez la, sinon, tapez 0 : "))
    texte_decode = ''

    if cle == 0 :
        banane = 1
    if cle != 0 :
        for lettre in texte_cripte :
            if lettre in alphabet :
                position = alphabet.index(lettre)
                nouvelle_position = (position + cle)%26
                texte_decode += alphabet[nouvelle_position]
            else :
                texte_decode += lettre

        print ('voici le texte decode : ', texte_decode)

choix_de_la_fonction()