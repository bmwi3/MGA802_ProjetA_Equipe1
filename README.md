# MGA802_ProjetA_Equipe1
Ce dépôt contient le rendu du projet A pour l'équipe 1.
Le projet consiste en un programme de chiffrement déchiffrement de code César.
Un rapport sera rendu séparement, il présentera la structure du programme, 
les stratégies retenues pour les algorithmes de brute force, l’évaluation de leur efficacité et la 
distribution des tâches au sein de l’équipe. 
 
# Objectifs du code
Les objectifs du code sont les suivant :
 - Le programme doit permettre de soit :
    - encrypter/décrypter des entrées fournies dans la console
    - encrypter/décrypter des fichiers textes dont le nom est fourni par l’utilisateur
 - Accepter n’importe quelle clé positive ou négative fournie par l’utilisateur pour 
l’encryptage ou le décryptage.
 - Fournir des messages clairs (requête, info, erreur) à l’utilisateur.
 - Proposer un mode brute force pour retrouver la clé


# Comment utiliser le code
Pour pouvoir utiliser le programme de César plusieurs options s'offrent à toi.
Attention dans tous les cas tu dois éxecuter le code dans le dossier dans lequel sont les fichiers.

## Clonage du dépot
1. Clique sur le bouton `Code` en haut à droite du dépot
2. Copie le lien
3. Ouvre ton IDE favori sur lequel est configuré git
4. Clone le dépot soit de manière graphique soit en utilisant :
   ```bash
   git clone <https://github.com/bmwi3/MGA802_ProjetA_Equipe1.git>
   ```
5. Ouvre le fichier `main.py`.
6. Execute-le, il n'y a plus qu'à suivre les instructions dans le terminal

## Téléchargement du fichier 
1. Télécharge directement le fichier `main.py` et `liste_français.txt`
2. Crée un dossier et mets les deux fichier à l'intérieur
3. Ouvre le dossier dans ton IDE favori et tu éxecute `main.py`

## Encodage-Decodage du fichier
Pour utiliser un fichier à encoder ou décoder il faut le mettre dans le même dossier que les fichier `main.py` et `liste_français.txt`

# Structure du code
Le code est decomposé en différentes fonctions : 
- `main()` est la fonction principale qui appelle toutes les autres fonctions. On y trouve aussi les consignes utilisateurs et des vérifications sur les retours des fonctions/sur les entrées utilisateurs.
- `sauvegarder_fichier()` et `ouvrir_fichier()` permettent la gestion des fichiers au sein du dossier contenant le code.
- `enlever_caracteres_speciaux()` permet de normaliser les entrées textes du code.
- `entree_utilisateur()` demande les informations a l'utilisateur et les traite pour pouvoir utiliser les fonctions d'encodage et de décodage.
- `encode_cesar()` cette fonction réalise l'encodage d'un texte en fonction d'une clé spécifier par l'utilisateur
- `decode_cesar()` realise le décodage du code en utilisant `encode_cesar()` en inversant la clé en paramètre.
- `brute_force_cesar()` utilise un décodage brute. La condition d'arrêt est en fonction du nombre de caractère similaire qui sont assimilé comme des e.
- `brute_force_cesar_manuel()` fonction qui teste toutes les clés que l'utilisateur souhaite essayer.
- `brute_force_dictionnaire()` deuxième fonction automatique de brute force qui fait appel à un dictionnaire.

# Structure du dépôt
Le dépot est composé de trois fichiers.
- Le ReadMe
- Le fichier `main.py` : fichier principale du rendu qui contient le code python
- Le fichier texte `liste_francais.txt` : utile pour la fonction de brute force qui utilise un dictionnaire français.

# Références
Le site <https://www.w3schools.com/python/python_file_write.asp> a été utilisé pour l'ouverture et la fermeture.

La méthode comptabilisant les e a été trouvé sur le site suivant : <https://www.dcode.fr/chiffre-cesar> 