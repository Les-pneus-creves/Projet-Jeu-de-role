import Evenement
import pygame
import pygame_menu
import Objet  # pour faire test
from EquipeDePersonnages import EquipeDePersonnages
from Personnage import Personnage  # pour faire test
from Recompense import Recompense
from Combat import Combat
from Inventaire import Inventaire
import Objet


class ModeEvenement:
    def __init__(self, evenement: Evenement, equipe: EquipeDePersonnages):
        self._evenement = evenement
        self._equipe = equipe
        self._loot = self._evenement.getLoot()
        if self._loot.vide():
            self._loot = None
        self._lootCoord = 500, 500
        self._objetSelectione = None
        self._enCours = True

    def getEvenement(self):
        return self._evenement

    # lecture des evenements
    def on_event(self, events, event) -> None:
        if self._evenement.getEnCours():
            if self._evenement.getMenu().is_enabled():
                self._evenement.getMenu().update(events)
        elif self._loot is not None:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = int(event.pos[0])  # Enregistre la coordonnée y de l'event
                y = int(event.pos[1])  # Enregistre la coordonnée y de l'event
                if self.isSurLaCroix((x, y)):
                    self._enCours = False
                elif self.isInOneInventory((x, y))[0]:
                    if self.isInOneInventory((x, y))[1] < 4:
                        personnageSelection = self._equipe.getPersonnages()[self.isInOneInventory((x, y))[1]]
                        if self._objetSelectione is None:
                            self._objetSelectione = personnageSelection.getObjetByCoord((x, y))
                            if self._objetSelectione is not None:
                                personnageSelection.removeFromInventaire(self._objetSelectione)
                        else:
                            objetDestination = personnageSelection.getObjetByCoord((x, y))
                            if objetDestination is None or objetDestination.getNom() == self._objetSelectione.getNom():
                                personnageSelection.addToInventaire(self._objetSelectione)
                                self._objetSelectione = None
                            else:
                                personnageSelection.removeFromInventaire(objetDestination)
                                personnageSelection.addToInventaire(self._objetSelectione)
                                self._objetSelectione = objetDestination
                    else:
                        if self._objetSelectione is None:
                            self._objetSelectione = self.getObjetByCoord((x, y))
                            if self._objetSelectione is not None:
                                self._loot.retirer(self._objetSelectione)
                        else:
                            objetDestination = self.getObjetByCoord((x, y))
                            if objetDestination is None:
                                self._loot.ajouter(self._objetSelectione)
                                self._objetSelectione = None
                            else:
                                self._loot.retirer(objetDestination)
                                self._loot.ajouter(self._objetSelectione)
                                self._objetSelectione = objetDestination
                    print("l'objet en main", self._objetSelectione)
        else:
            pass

    # Calcul des mises à jours
    def on_loop(self) -> None:
        if not self._evenement.getEnCours():
            if self._loot is None:
                self._enCours = False

    # Calcul des affichages
    def on_render(self, window) -> None:
        if self._evenement.getEnCours():
            if self._evenement.getMenu().is_enabled():
                self._evenement.getMenu().draw(window)
        else:
            self._equipe.renderPersonnageInventaire(window)
            if self._loot is not None:
                self._loot.render(window, self._lootCoord[0], self._lootCoord[1])
            pygame.draw.rect(window, (255, 0, 0), (self._lootCoord[0] - 60, self._lootCoord[1], 60, 60))
            pygame.draw.line(window, (0, 0, 0), (self._lootCoord[0] - 60, self._lootCoord[1]), (self._lootCoord[0], self._lootCoord[1] + 60))
            pygame.draw.line(window, (0, 0, 0), (self._lootCoord[0] - 60, self._lootCoord[1] + 60), (self._lootCoord[0], self._lootCoord[1]))

    def getEnCours(self):
        return self._enCours

    def getVictoire(self):
        return self._evenement.getVictoire()

    def isInOneInventory(self, coord: tuple):
        """Méthode pour savoir si le clic se trouve dans un `src.Inventaire` et si oui dans lequel"""
        if self.isInLoot(coord):
            return True, 4

        peronnages = self._equipe.getPersonnages()
        i = 0
        for peronnage in peronnages:
            if peronnage.isInInventory(coord):
                return True, i
            i += 1
        return False, i

    def isInLoot(self, coord: tuple):
        return self._lootCoord[0] <= coord[0] <= (self._lootCoord[0] + (4 * 60)) and self._lootCoord[1] <= coord[1] <= (self._lootCoord[1] + 60)

    def isSurLaCroix(self, coord: tuple):
        return (self._lootCoord[0] - 60) <= coord[0] <= self._lootCoord[0] and self._lootCoord[1] <= coord[1] <= (self._lootCoord[1] + 60)

    def getObjetByCoord(self, point: tuple):
        if self.isInLoot(point):
            coord = int((point[0] - self._lootCoord[0]) / 60), int((point[1] - (self._lootCoord[1] + 60)) / 60)
            index = coord[0] + (coord[1] * 4)
            return self._loot[index].getObjet()
        return None


if __name__ == "__main__":

    pygame.init()

    window = pygame.display.set_mode((1000, 1000), pygame.HWSURFACE | pygame.DOUBLEBUF)

    jean = Personnage("Jean", 15, 7, 8, 15, None)
    bob = Personnage("Bob", 10, 8, 6, 12, None)
    jeanCastex = Personnage("JeanCastex", 12, 9, 4, 4, None)
    pz = Objet.Arme("Arme_Panzerschreck", "src/images/Objets/Panzerschreck.png", 25, 2)
    bob.addToInventaire(pz)

    equipe = EquipeDePersonnages(jean, bob, jeanCastex)

    c = Combat(equipe)

    evenement = c

    c.lancement()
    x = ModeEvenement(evenement)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if evenement.getEnCours():

            if x.getEvenement().getMenu().is_enabled():
                x.getEvenement().getMenu().update(events)
                x.getEvenement().getMenu().draw(window)

        # else:
        # pygame.draw.rect(window, (255,0,0),(0,0,1000,1000))
        pygame.display.flip()
