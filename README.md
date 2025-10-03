# Projet Arbre Binaire de Recherche (ABR)

## Membres du groupe
- Tiavina L1C 228 : Partie 1 (structure de base)  
- Steeve  L1C 225: Partie 2 (insertion)  
- Hariniaina L1C 226: Partie 3 (recherche, parcours, programme principal)  

---

## Objectif du projet
Le but est de créer un **Arbre Binaire de Recherche (ABR)** en Python.  
Un ABR est une structure de données où chaque nœud contient :  
- une **valeur**  
- un lien vers un **sous-arbre gauche** (valeurs plus petites)  
- un lien vers un **sous-arbre droit** (valeurs plus grandes)  

Cela permet de **stocker et rechercher efficacement des données numériques**.

---

## Organisation du projet
- `partie1_debut.py` → Création de la classe `Noeud` et de la classe `ABR` (structure de base).  
- `partie2_insertion.py` → Ajout de la fonction `inserer` pour insérer des valeurs dans l’ABR.  
- `partie3_fin.py` → Ajout de la fonction `rechercher`, du parcours infixe et d’un programme principal.  

Chaque membre du groupe a contribué en ajoutant une partie dans un commit séparé.

---

## Fonctionnalités principales
1. **Création d’un arbre binaire de recherche**  
2. **Insertion de nouvelles valeurs** dans l’arbre  
3. **Recherche d’une valeur** (retourne `True` ou `False`)  
4. **Parcours infixe** → affiche les valeurs de l’arbre dans l’ordre croissant  

---

##  Exemple d’exécution
```bash
$ python3 abr_structure.py
```

### Résultat attendu :
```
Parcours infixe :
3 5 7 10 15 20 
Recherche 7 : True
Recherche 100 : False
```

---

## Explication simple
- L’ABR commence avec une racine (`racine`).  
- Chaque valeur ajoutée est comparée :  
  - si elle est plus petite → elle va à gauche  
  - si elle est plus grande → elle va à droite  
- Grâce à cette règle, les recherches et l’affichage trié deviennent faciles.  

Exemple de l’arbre avec nos valeurs :

```
        10
       /  \
      5    20
     / \   /
    3   7 15
```

---

## Ce que nous avons appris
- Manipuler des **classes** et des **objets** en Python  
- Comprendre une structure de données classique (ABR)  
- Travailler en **groupe avec Git et GitHub** en faisant plusieurs commits  
