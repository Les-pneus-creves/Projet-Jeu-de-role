class Expedition:

    def __init__(self, equipe, plateau):
        self.__temps = 1             #Numéro du tour de l'expédition en cour
        self.__equipe = equipe          #Equipe de personnage joueur du joueur
        self.__eventEnCours = None      #Evenement actuellement en cours
        self.__plateau = plateau     #Plateau sur lequel l'éxpedition se déroule

    # lecture des evenements
    def on_event(self, event):
        pass
    
    #Calcul des mises à jours
    def on_loop(self):
        pass
    
    #Calcul des affichages
    def on_render(self, window):
        pass
        

    #Méthode lançant un événement précis
    def lancerEvenement(self,evenement):
        pass


    #Méthode retournant true ou false selon si des coordonnées (En pixel ou en case/hexagone??) sont effectivement dans la map
    def estDansLaMap(self,coord):
        pass

    