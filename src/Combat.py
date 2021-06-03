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

        with open("src/dossierJson/combats.json") as fichier:
            data = json.loads(fichier.read())
            combat_a_lancer = random.choice(list(data))
            self.eventJson = data[combat_a_lancer]

        self._log = []
        self._menu = None
        self._equipeMechant: EquipeDePersonnages = self.creerEquipeMechant(self.eventJson)
        self._equipe = equipe

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

        self.creerMenuCombat(logs)
        self.creerMenu(self.eventJson["titre"], self.eventJson["texte"], self.eventJson["image"])

        # Methode appelée dans l'init qui modifie le menu avec ce qu'il faut

    def creerMenu(self, titre: str, texte: str, image) -> None:

        # création du menu "principal"

        self._menu = pygame_menu.Menu(titre, 1000, 1000)
        self._menu.add.label(texte)
        self._menu.add.image(image)
        self._menu.add.button("Voir logs", self._log)
        self._menu.add.button("ok", self.mettreFin)

    def creerMenuCombat(self, logs):
        # création du menu log
        self._log = pygame_menu.Menu("logs de combat", 1000, 1000, center_content=False)
        for entree in logs:
            self._log.add.label(entree, align=pygame_menu.locals.ALIGN_LEFT)
        self._log.add.button("Retour", pygame_menu.events.BACK)

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

    # Methode qui retourne une equipe de personnage en fonction du combat lancé
    def creerEquipeMechant(self, combat):

        equipetemp = []
        if combat["unite"]["nom"] == "Kv2v2v2":
            nb = 1
        else:
            nb = random.randint(1, 3)

        for i in range(nb):
            equipetemp.append(self.creerMechant(combat["unite"], i))

        if nb == 1:
            return EquipeDePersonnages(equipetemp[0])
        elif nb == 2:
            return EquipeDePersonnages(equipetemp[0], equipetemp[1])
        else:
            return EquipeDePersonnages(equipetemp[0], equipetemp[1], equipetemp[2])

    # Methode qui creer un mechant avec les valeurs aléatoire du json
    def creerMechant(self, modele, i: int):

        vie = random.randint(modele["vieMin"], modele["vieMax"])
        force = random.randint(modele["forceMin"], modele["forceMax"])
        ini = random.randint(modele["iniMin"], modele["iniMax"])
        preci = random.randint(modele["preciMin"], modele["preciMax"])

        return Personnage(modele["nom"] + " " + str(i+1), vie, force, preci, ini, None)

    # Méthode permmetant de selectionné une cible dans une équipe donnée
    def _choisirCible(self, equipePerso: EquipeDePersonnages) -> Personnage:
        cible = random.choice(equipePerso.getPersonnagesVivants())
        return cible

    def faireAttaquer(self, attaquant: Personnage, cible: Personnage) -> str:
        pourLog = attaquant.attaquer(cible)

        if pourLog == 0:
            return "\"" + str(attaquant.getNom()) + "\" attaque \"" + str(cible.getNom()) + "\" mais loupe!"

        if cible.getVie() > 0:
            return "\"" + str(attaquant.getNom()) + "\" attaque \"" + str(cible.getNom()) + "\" pour " + str(
                pourLog) + " points de dégats. " + str(cible.getNom()) + " a : " + str(cible.getVie()) + "pv"
        else:
            return "\"" + str(attaquant.getNom()) + "\" attaque \"" + str(cible.getNom()) + "\" pour " + str(
                pourLog) + " points de dégats. \"" + str(cible.getNom()) + "\" est mort"


if __name__ == "__main__":
    # création d'une équipe

    jean = Personnage("Jean", 15, 10, 8, 2, "image")
    bob = Personnage("Bob", 10, 10, 6, 4, "image")
    jeanCastex = Personnage("JeanCastex", 12, 10, 4, 6, "image")

    equipe = EquipeDePersonnages(jean, bob, jeanCastex)

    c = Combat(equipe)

    print("combatfait")

    c.lancement()

    print(c._log)

    print("fini")
