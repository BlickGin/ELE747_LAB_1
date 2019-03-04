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

### Validation 

## Obtention du programme

### Prérequis


  * [Python 3.5](https://www.python.org/downloads/release/python-370/)


  
  * [PIP](https://pypi.org/project/pip/)



  * [Numpy](https://pypi.org/project/numpy/)



  * [Pickle](https://pypi.org/project/pickle5/)



  * [Tkinter](https://pypi.org/project/tkinter3000/)
  


  * [Pygubu](https://pypi.org/project/pygubu/)


### Installation


## Déploiment


## Auteurs

* **André-Philippe Audette**
* **André-Philippe Audette**
* **André-Philippe Audette**

