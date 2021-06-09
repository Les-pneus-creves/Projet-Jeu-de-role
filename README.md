# Projet-Jeu-de-role
Jeu de rôle post apocalyptique 2nd guerre mondiale de Thomas CHAMPSEIX et Gabriel MASSCHELEIN

## Instruction d'installation :

Pour faire tourner le jeu, il vous faudra avoir installé :
* Python 3.8.5 (seule version testée en développement) 
* Pygame 2.0.1 (via pip3 : `pip3 install pygame`)
* PyTMX 3.24 (via pip3 : `pip3 install PyTMX`)
* pygame_menu 4.0.2 (via pip3 : `pip3 install pygame-menu`)

## Instruction de lancement : 

Il suffit en suite de lancer le fichier Jeu.py depuis la racine du projet avec Python 3.8.5 :
    `python3.8 src/Jeu.py`

## Instruction de mise à jour de la doc :

Voici la commande pour générer la doc :
`pdoc --html src/ --output-dir doc/ --force`