# Laboratoire : MLP

Ce projet est le second laboratoire du cours ELE-767 : Apprentissage machine en intelligence artificielle. L'objectif est de créer,
entraîner et tester un perceptron multicouche pour que celui-ci puisse identifier des sons produits par la voix humaines. Ces sons
sont des chiffres de 1 à 10 qui doivent être traités par le programme et identifiés selon le chiffre audible.

## Fonctionnement général

### Perceptron multicouche

Le perceptron multicouche permet de résoudre les relations entre l'entrée et la sortie pour des système non-linéairement séparable. Le principe est de créer un réseau de neuronnes réparties sur plusieurs couches pour transformer un vecteur d'entrée X en un vecteur de sortie Y de dimension moindre. 

### Données d'identification d'un son

Les données utilisées pour représenter un son de la voix humaines sont des fichiers de texte. Où chaque ligne du fichier représente un son selon le format suivant : 

<p align="center">1: (S1 S2 .. S11 S12 ES1 D1 D2 .. D11 D12 ED1) x60</p>
        
Donc la donnée du son 'one' (1:) possède : 
* 12 valeurs d'amplitudes statiques
* 1  valeur d'énergie statique
* 12 valeurs d'amplitudes dynamique
* 1 valeurs d'énergie dynamique
        
Et ce sur 60 cadres d'analyse.

On peut alors définir un premier vecteur d'entrée X. 

On suppose d'abord qu'on utilise toutes les données dans le vecteur d'entrée on a alors un vecteur de 26 données multiplier par 60 cadres d'analyse ce qui donne 1560 données dans le vecteur X.

### Validation 

Pour valider l'entrainement du réseau de neuronnes on utilise trois types de données
1. Les données d'entrainement.

    * Ces données servent à entrainé le réseau on peut les utilisés comme première approximation de l'apprentissage du réseau, par contre on doit utilisé d'autre donnés pour la validation afin d'éviter le surapprentissage.
2. Les données de validation croisée.

    * Ces données sont différentes des données d'apprentissage et permettent de déduire un apprentissage réel du réseau.
3. Les données de test.

    * Une fois que l'on juge l'apprentissage du réseau suffisant, on le test sur des données de tests qui sont différentes de celles de la validation croisée et de l'apprentissage.
## Obtention du programme


### Prérequis

Note : Un script d'installation est fournie dans le .zip (windows only) sous le nom de Install_Package.bat les détails sont dans la section installation plus bas.


  * [Python 3.7](https://www.python.org/downloads/release/python-370/)


  
  * [PIP](https://pypi.org/project/pip/)



  * [Numpy](https://pypi.org/project/numpy/)



  * [Pickle](https://pypi.org/project/pickle5/)



  * [Tkinter](https://pypi.org/project/tkinter3000/)
  


  * [Pygubu](https://pypi.org/project/pygubu/)
  
  
  
  * [Matplotlib](https://matplotlib.org/)


### Installation

Le script Install_Package.bat utilise l'invite de commande windows pour installer divers modules python à l'aide de l'utilitaire PIP. Il est à noté qu'à partir de la version 3.4 de Python PIP est installé par défaut lors de l'installation de Python. Donc le seul prérequis à l'installation sur windows est alors Python 3.7. L'installation se déroule donc comme suit : 

        1. Télécharger le fichier .zip contenant le code. 
        2. Télécharger Python3.7.
        3. Extraire le .zip dans un dossier quelconque.
        4. Lancer le fichier Install_Package.bat
        5. Normalement l'installation devrait être complète.

## Déploiment

Pour lancer le programme, il suffit de lancer le fichier Gui.py dans le dossier ou le .zip a été extrait.Puis, de cliquer sur l'option New Network, selectionner le nombre de couches cachées, la configuration du vecteur d'entrée et le type de fonction d'activation. Une fois cela fait dans Network list selectionner Network_2.pkl, puis appuyer sur Start_learning pour commencer l'entrainement.Ensuite, attendez durant quelques heures (Notre programme est vraiment TRÈS lent) et une fois l'entrainement terminé appuyer sur le bouton Start Testing pour vérifier le performance du réseau avec les données de test.

## Auteurs

* **André-Philippe Audette**
* **Noah Ploch**
* **Aurélien Laurent**

