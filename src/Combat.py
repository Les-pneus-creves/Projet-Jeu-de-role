from abc import ABC, abstractmethod  # module pour classe abstraite
from Evenement import Evenement  # Heritage
from EquipeDePersonnages import EquipeDePersonnages
from Personnage import Personnage
# import Personnage
import pygame_menu
import json
import pygame
import random
from Inventaire import Inventaire
import Objet


class Combat(Evenement):

    def __init__(self, equipe: EquipeDePersonnages, combat_a_lancer: str = None):
        """ Un `Combat` fait combattre l'équipe de personnages joueurs et une équipe de méchant créée par le combat.

            Parameters
            ----------
            equipe : `EquipeDePersonnages`
                Equipe de personnage joueur
            combat_a_lancer : str
                Optionel: Permet de forcer un type de combat.
        """
        super().__init__()

        with open("src/dossierJson/combats.json") as fichier:
            data = json.loads(fichier.read())
            if combat_a_lancer is None:
                combat_a_lancer = random.choice(list(data))
            self.eventJson = data[combat_a_lancer]

        self.nom = combat_a_lancer
        self._log = []
        self._menu = None
        self._equipeMechant: EquipeDePersonnages = self.creerEquipeMechant(self.eventJson)
        self._equipe = equipe

    def lancement(self):
        """ Méthode qui déroule la logique de combat"""

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
            logs.append("Les méchants ont gagné")
            self._victoire = False
        else:
            logs.append("Les gentils ont gagné")

        self.creerMenuCombat(logs)
        self.creerMenu(self.eventJson["titre"], self.eventJson["texte"], self.eventJson["image"])


    def creerMenu(self, titre: str, texte: str, image) -> None:
        """Methode appelée dans l'init qui crée le menu du combat avec les infos du combat

        Parameters
        ----------
        titre: str
            Titre du combat
        texte: str
            Texte du combat
        image: pygame.image
            Image du combat

        Retourne None
        """

        taille = list(pygame.display.get_window_size())
        taille[0] /= 1.25
        taille[1] /= 1.25
        self._menu = pygame_menu.Menu(titre, taille[0], taille[1])
        self._menu.add.label(texte)
        self._menu.add.image(image)
        self._menu.add.button("Voir logs", self._log)

    def creerMenuCombat(self, logs):
        """ Création du menu de logs.

        Parameters
        ----------

        logs: str[]
            Array de string

        Retourne None

        """
        taille = list(pygame.display.get_window_size())
        taille[0] /= 1.25
        taille[1] /= 1.25
        self._log = pygame_menu.Menu("logs de combat", taille[0], taille[1], center_content=False)
        for entree in logs:
            self._log.add.label(entree, align=pygame_menu.locals.ALIGN_LEFT)
        self._log.add.button("Quitter", self.mettreFin)

    def mettreFin(self):
        """ Methode mettant fin a l'évenement combat

        Retourne None
        """
        self._enCours = False
        self._menu._close()

    def __creerOrdreTour(self, ep1: EquipeDePersonnages, ep2: EquipeDePersonnages) -> list:
        """ Méthode permettant de faire une liste de personnage par initiative décroissante à partir de 2 `EquipeDePersonnages`

         Parameters
         ----------

         ep1: `EquipeDePersonnages`
         ep2: `EquipeDePersonnages`

        Retourne list[`Personnage`]
         """
        listeDesordre = ep1.getPersonnages() + ep2.getPersonnages()
        listeOrdre = []

        for i in range(len(listeDesordre)):
            persoTemp = self.getInitmax(listeDesordre)
            listeOrdre.append(persoTemp)
            listeDesordre.remove(persoTemp)

        return listeOrdre

    def getInitmax(self, ep: list) -> Personnage:
        """ Methode qui retourne le personnage ayant la plus grande initiative dans une liste de personnage

        Parameters
        ----------

        ep: list[`Personnage`]
            Liste de personnages

        Retourne Une liste de personnage triée par initiative décroissant

        """
        persoReturned = ep[0]

        for perso in ep:
            if perso.getInitiative() > persoReturned.getInitiative():
                persoReturned = perso

        return persoReturned

    def creerEquipeMechant(self, combat):
        """  Methode qui retourne une equipe de personnage en fonction du combat a lancer

        Parameters
        ----------
        combat: Dictionnaire
            Dictionnaire qui contient les données du combat (Par exemple les ennemis a instancier)

        Retourne None
        """
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

    def creerMechant(self, modele, i: int):
        """ Methode qui creer un personnage "mechant" avec les valeurs aléatoire du json

        Parameters
        ----------
        modele: Dictionnaire
            Dictionnaire qui contient les fourchettes de stats pour le personnage a créer

        i: int
            Int permettant d'incrémenter le nom du personnage

        retourne un `src.Personnage`
        """
        vie = random.randint(modele["vieMin"], modele["vieMax"])
        force = random.randint(modele["forceMin"], modele["forceMax"])
        ini = random.randint(modele["iniMin"], modele["iniMax"])
        preci = random.randint(modele["preciMin"], modele["preciMax"])

        return Personnage(modele["nom"] + " " + str(i+1), vie, force, preci, ini, None)

    def _choisirCible(self, equipePerso: EquipeDePersonnages) -> Personnage:
        """ Méthode permmetant de selectionné une cible dans une équipe donnée

        Parameters
        ----------
        equiperPerso: `EquipeDePersonnage`
            Equipe dans laquelle on cherche une cible

        Retourne une `Personnage` selectionné aléatoirement
        """
        cible = random.choice(equipePerso.getPersonnagesVivants())
        return cible

    def faireAttaquer(self, attaquant: Personnage, cible: Personnage) -> str:
        """ Methode appelant la méthode attaquer d'un `Personnage` et retourne un string pour construire le log

        Parameters
        ----------
        attaquant: `Personnage`
            `Personnage` attaquant
        cible: `Personnage`
            `Personnage` ciblé

        retourne un string
        """
        pourLog = attaquant.attaquer(cible)

        if pourLog == 0:
            return "\"" + str(attaquant.getNom()) + "\" attaque \"" + str(cible.getNom()) + "\" mais loupe!"
        elif pourLog == -1:
            return "\"" + str(attaquant.getNom()) + "\" attaque sans arme antichar \"" + str(cible.getNom()) +"\""

        if cible.getVie() > 0:
            return "\"" + str(attaquant.getNom()) + "\" attaque \"" + str(cible.getNom()) + "\" pour " + str(
                pourLog) + " points de dégats. " + str(cible.getNom()) + " a : " + str(cible.getVie()) + "pv"
        else:
            return "\"" + str(attaquant.getNom()) + "\" attaque \"" + str(cible.getNom()) + "\" pour " + str(
                pourLog) + " points de dégats. \"" + str(cible.getNom()) + "\" est mort"

    def getLoot(self):
        """Methode qui retourne un `src.Inventaire `de deux objets en fonction du loot possible au combat.

        Return
        ------
        inv: `src.Invetaire`
            inventaire lootable par le joueur.

        """

        listeObjet = self.eventJson["loot"]

        inv = Inventaire(0,0,4)

        if len(listeObjet) > 0:
            for i in range(2):
                objet = random.choice(listeObjet)
                if objet == "Patate":
                    inv.ajouter(Objet.objets[objet], random.randint(1,7))
                else:
                    inv.ajouter(Objet.objets[objet])
        return inv





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
