# Recuit simulé – Optimisation

Ce dépôt contient une implémentation en Python de l’algorithme du **recuit simulé**, une méta-heuristique d’optimisation inspirée d’un phénomène physique utilisé en métallurgie.

## 📌 Description
Le recuit simulé est une méthode d’optimisation permettant de rechercher un **minimum global** d’une fonction, même en présence de plusieurs minima locaux.  
Il repose sur l’acceptation probabiliste de solutions moins bonnes afin d’éviter le piégeage dans des minima locaux.

## ⚙️ Principe de l’algorithme
- Initialisation d’une solution de départ
- Exploration du voisinage de la solution courante
- Acceptation automatique des solutions améliorantes
- Acceptation probabiliste de solutions dégradantes selon le critère de Metropolis
- Diminution progressive de la température (refroidissement)
- Convergence vers une solution optimale globale

## 📊 Exemple d’application
L’algorithme est appliqué à la fonction suivante :
\[
f(x) = \cos(x) + 0.05x^2
\]

Une visualisation permet d’illustrer la fonction ainsi que le minimum global trouvé par l’algorithme.

## 🛠️ Technologies utilisées
- Python
- NumPy
- Matplotlib

## 👥 Auteurs
- Salma Belaalia
- Houda Elbasit
