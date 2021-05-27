from abc import ABC, abstractmethod  # module pour classe abstraite
from Evenement import Evenement  # Heritage
from EquipeDePersonnages import EquipeDePersonnages
from Personnage import Personnage
# import Personnage
import pygame_menu
import json
import pygame
import random

class Combat(Evenement):

    def __init__(self, equipe: EquipeDePersonnages):
        super().__init__()

        dude = Personnage("Dude", 150, 50, 4, 6, "image") #pour test....
        dude2 = Personnage("Dude2", 12, 10, 4, 6, "image")  # pour test....

        self._log = []
        self._menu = None
        self._equipeMechant: EquipeDePersonnages = EquipeDePersonnages(dude)  # pour test
        self._equipe = equipe
        self.eventJson = []

        with open("src/dossierJson/combats.json") as fichier:
            data = json.loads(fichier.read())
            event_a_lancer = random.choice(list(data))
            self.eventJson = data[event_a_lancer]

    # ----------


    def getMenu(self):
        return self._menu


    # Méthode permettant de donner au combat l'équipe de personnage Joueur qui va se battre et déroule la logique de combat
    def lancement(self):
        logs = []
        m = self._equipeMechant
        g = self._equipe
        listeOrdre = self.__creerOrdreTour(m, g)

        while m.getVivante() and g.getVivante():
            print(self._equipe)
            for perso in listeOrdre:
                if perso.estVivant():
                    if perso in m.getPersonnages() and g.getVivante():
                        logs.append(self.faireAttaquer(perso, self._choisirCible(g)))
                    elif perso in g.getPersonnages() and m.getVivante():
                        logs.append(self.faireAttaquer(perso, self._choisirCible(m)))
        if m.getVivante():
            logs.append("Les méchant on gagné bruuuuh")
        else:
            logs.append("Les gentils ont gagné brubrubrubru")


       # pour test plutot que faire les menu je met juste les logs dans une variable lolg pour la print:

        self._log = logs
       # self.creerMenu(self.eventJson["titre"], self.eventJson["texte"], self.eventJson["image"])

       # self.creerMenuCombat(logs)


        # Methode appelée dans l'init qui modifie le menu avec ce qu'il faut

    def creerMenu(self, titre: str, texte: str, image) -> None:

        # création du menu "principal"

        self._menu = pygame_menu.Menu(titre, 1000, 1000)
        self._menu.add.label(texte)
        self._menu.add_image(image)
        self._menu.add_button("Voir logs", self._log)
        self._menu.add_button("ok", self.mettreFin)

    def creerMenuCombat(self, logs):
        # création du menu log
        self._log = pygame_menu.Menu("logs de combat", 1000, 1000, center_content=False)
        for entree in logs:
            self._log.add.label(entree, align=pygame_menu.locals.ALIGN_LEFT)
        self._log.add_button("Retour", pygame_menu.events.BACK)

    # Methode permettant de passer en cours a false
    def mettreFin(self):
        self._enCours = False
        self._menu._close()

    # Méthode permettant de déterminer l'ordre des tours des personnages lors du combat
    def __creerOrdreTour(self, ep1: EquipeDePersonnages, ep2: EquipeDePersonnages) -> list:


        listeDesordre = ep1.getPersonnages() + ep2.getPersonnages()
        listeOrdre = []

        for i in range(len(listeDesordre)):
            persoTemp = self.getInitmax(listeDesordre)
            listeOrdre.append(persoTemp)
            listeDesordre.remove(persoTemp)

        return listeOrdre

    def getInitmax(self, ep: list) -> Personnage:
        persoReturned = ep[0]

        for perso in ep:
            if perso.getInitiative() > persoReturned.getInitiative():
                persoReturned = perso

        return persoReturned




    # Méthode permmetant de selectionné une cible dans une équipe donnée
    def _choisirCible(self,equipePerso: EquipeDePersonnages) -> Personnage:
       cible = random.choice(equipePerso.getPersonnagesVivants())
       return cible


    def faireAttaquer(self, attaquant: Personnage, cible: Personnage) -> str :
        pourLog = attaquant.attaquer(cible)

        if cible.getVie() > 0:
            return str(attaquant.getNom()) + " attaque " + str(cible.getNom()) + " pour " + str(pourLog[0]) + " points de dégats. " + str(cible.getNom()) + " en reçoit : " + str(pourLog[1]) + "pv restant : " + str(cible.getVie())
        else:
            return str(attaquant.getNom()) + " attaque " + str(cible.getNom()) + " pour " + str(pourLog[0]) + " points de dégats. " + str(cible.getNom()) + " en reçoit : " + str(pourLog[1]) + " et meurt"


if __name__ == "__main__":



    #création d'une équipe

    jean = Personnage("Jean", 15, 10, 8, 2,"image")
    bob  = Personnage("Bob", 10, 10, 6, 4,"image")
    jeanCastex = Personnage("JeanCastex", 12, 10, 4, 6, "image")


    equipe = EquipeDePersonnages(jean, bob, jeanCastex)


    c = Combat(equipe)

    print("combatfait")

    c.lancement()

    print(c._log)

    print("fini")



