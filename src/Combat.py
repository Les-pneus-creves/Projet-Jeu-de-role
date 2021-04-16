from abc import ABC, abstractmethod  # module pour classe abstraite
from Evenement import Evenement  # Heritage
from EquipeDePersonnages import EquipeDePersonnages
# import Personnage
import pygame_menu
import json
import pygame
import random
from persotest import persotest


class Combat(Evenement):

    def __init__(self, equipe: EquipeDePersonnages):
        super().__init__()
        self._log = None
        self._equipeMechant: EquipeDePersonnages = persotest("arthur", 80, 1)  # J'ai mis none en attendant
        self._equipe = equipe

        with open("src/dossierJson/combats.json") as fichier:
            data = json.loads(fichier.read())
            event_a_lancer = random.choice(list(data))
            eventJson = data[event_a_lancer]
            self.creerMenu(eventJson["titre"], eventJson["texte"], eventJson["image"], self.lancement(self._equipe))

    # ----------

    # Méthode permettant de donner au combat l'équipe de personnage Joueur qui va se battre
    def lancement(self, equipePerso: EquipeDePersonnages) -> list:
        logs = []
        m = self._equipeMechant
        g = equipePerso

        while self._equipeMechant.getVivant() and equipePerso.getVivant():
            logs.append(m.faireDegat(m.getDegat(), g))
            if g.getVivant():
                logs.append(g.faireDegat(g.getDegat(), m))

        return logs

        # Methode appelée dans l'init qui modifie le menu avec ce qu'il faut

    def creerMenu(self, titre: str, texte: str, image, logs) -> None:

        # création du menu log
        self._log = pygame_menu.Menu("logs de combat", 1000, 1000, center_content=False)
        for entree in logs:
            self._log.add.label(entree, align=pygame_menu.locals.ALIGN_LEFT)
        self._log.add_button("Retour", pygame_menu.events.BACK)

        # création du menu "principal"

        self._menu = pygame_menu.Menu(titre, 1000, 1000)
        self._menu.add.label(texte)
        self._menu.add_image(image)
        self._menu.add_button("Voir logs", self._log)
        self._menu.add_button("ok", self.mettreFin)

    # Methode permettant de passer en cours a false
    def mettreFin(self):
        self._enCours = False
        self._menu._close()

    # Méthode permettant de déterminer l'ordre des tours des personnages lors du combat
    def __creerOrdreTour(self, ep1: EquipeDePersonnages, ep2: EquipeDePersonnages) -> list:

        listeDesordre = ep1.getPersonnages() + ep2.getPersonnages()
        listeOrdre = []

        for i in range(len(listeDesordre)):
            persoTemp = getInitmax(listeDesordre)
            listeOrdre.append(persoTemp)
            listeDesordre.remove(persoTemp)

        return listeOrdre

    def getInitmax(self, ep: list[Personnage]) -> Personnage:
        persoReturned = ep[1]

        for perso in ep:
            if perso.getInitiative() > persoReturned.getInitiative():
                persoReturned = perso

        return persoReturned




    # Méthode permmetant de selectionné une cible dans une équipe donnée
    def __choisirCible(self,equipePerso: EquipeDePersonnages) -> Personnage:
       pass

