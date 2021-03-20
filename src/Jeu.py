import pygame
from enum import Enum
import Expedition
import PlateauDeJeu


Etats = Enum('Etats', 'Gestion Expedition Evenement')

class Jeu:
    def __init__(self):
        self.__nbTour = 0    
        self.__running = True
        self.__size = self.width, self.height = 720, 720
        self.__window = None
        self.__etatActuel = Etats.Expedition
        self.__expedition = Expedition(equipe, PlateauDeJeu("maps/1.tmx"))

    #Méthode lancée une fois servant a initialisé tout ce qu'il faut
    def on_init(self):
        pygame.init()
        self.__window = pygame.display.set_mode(self.__size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.__running = True
    
    #Méthode définissant la boucle de jeu principale
    def on_execute(self):
        if self.on_init() == False:
            self.__running = False
 
        while(self.__running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    # lecture des evenements
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False
        
        if self.__etatActuel == Etats.Gestion:
            pass
        elif self.__etatActuel == Etats.Expedition:
            self.__expedition.on_event()
        elif self.__etatActuel == Etats.Evenement:
            pass
        else:
            print("Etat inexistant dsl ...")

    #Calcul des mises à jours
    def on_loop(self):
        
        if self.__etatActuel == Etats.Gestion:
            pass
        elif self.__etatActuel == Etats.Expedition:
            self.__expedition.on_loop()
        elif self.__etatActuel == Etats.Evenement:
            pass
        else:
            print("Etat inexistant dsl ...")

    #Calcul des affichages
    def on_render(self):
        
        if self.__etatActuel == Etats.Gestion:
            pass
        elif self.__etatActuel == Etats.Expedition:
            self.__expedition.on_render()
        elif self.__etatActuel == Etats.Evenement:
            pass
        else:
            print("Etat inexistant dsl ...")
        pygame.display.flip()
        pass

    #Méthode pour quitter le jeu proprement  
    def on_cleanup(self):
        pygame.quit()



if __name__ == "__main__" :
    leJeu = Jeu()
    leJeu.on_execute()