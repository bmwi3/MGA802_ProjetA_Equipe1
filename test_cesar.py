

#  Analyse fréquentielle (repérer les lettres les plus courantes) : 
# les langues ont des fréquences de lettres caractéristiques. 
# La lettre E est la plus courante. 
# Si une autre lettre apparaît très souvent dans le texte chiffré, 
# il s'agit probablment d'un E décalé. En calculant la différence entre cette lettre et le E, il est possible de retrouver le décalage.

# Exemple : Si la lettre X est la plus fréquente. Comme X est 19 rangs après E dans l'alphabet, 
# cela signifie que le texte a probablement été chiffré avec un décalage de 19.

#premiere logique qui soccupe de tester les 25 combinaisons

### Fct de test 
def encode_cesar(text, shift):
    texte_encode = ""
    for char in text:
        if char.isalpha():
            # Décalage de la lettre
            decalage = ord(char) + shift
            # Si le décalage dépasse 'Z', on revient au début de l'alphabet
            if char.isupper() and decalage > ord('Z'):
                decalage -= 26
            elif char.islower() and decalage > ord('z'):
                decalage -= 26
            texte_encode += chr(decalage)
        else:
            texte_encode += char
    return texte_encode

def decode_cesar(text, shift):
    return encode_cesar(text, -shift)


alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


####

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
        print(score)
        if score > meilleur_score:
            meilleur_score = score
            texte_devine = texte_decode
            meilleure_decalage = decalage

    return texte_devine, meilleure_decalage, meilleur_score

def brute_force_cesar_manuel(text):
    while True:
        decalage = int(input("choisir le décalage: "))
        texte_decode = decode_cesar(text, decalage%26)
        print(texte_decode)
        retour_utilisateur = input("le resultat vous convient-il ? (o/n)")
        if retour_utilisateur.lower() == 'o':
            break
        else:
            print("Essayez un autre décalage.")
        
        #si oui on sort de la boucle

text="Mh v’dsshooh jurrw"

print(brute_force_cesar(text))

#brute_force_cesar_manuel(text)
#methode avec mot_clé
#peut donner une valeurs a chaque lettre

#compte les enchainements de lettres
#

