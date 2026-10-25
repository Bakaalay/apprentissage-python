def compteur_mots(phrase):
    """
    Compte le nombre de mots dans un texte donné.

    Args:
        texte (str): Le texte à analyser.

    Returns:
        int: Le nombre de mots dans le texte.
    """
    compteur={}
    
    # On utilise la méthode split() pour diviser la phrase en mots
    mots = phrase.split()

    #on prépare les mots en retirant toute ponctuation à la fin de chaque mot
    for i in range(len(mots)):
        mots[i] = mots[i].rstrip('.,;!?')

    #on parcourt la liste de mots et on compte le nombre d'occurrences de chaque mot
    for mot in mots:
        #si le mot existe on incrémente de 1
        if mot in compteur:
            compteur[mot] += 1
        else:
            #si le mot n'existe pas on l'ajoute au dictionnaire avec une valeur de 1
            compteur[mot] = 1
            
    # On retourne le dictionnaire 
    return compteur

phrase = "le chat mange le poisson et le chien mange la viande"
print(compteur_mots(phrase))

resultat = compteur_mots(phrase)
classement = sorted(resultat.items(), key=lambda x: x[1], reverse=True)

for mot, nombre in classement[:3]:
    print(mot, ":", nombre)