class ModeEvenement:
    def __init__(self):
        self.__evenement = None    #Evenement actuellement en cours (peut etre nul)

    # lecture des evenements
    def on_event(self, event) -> None:
        pass
    
    #Calcul des mises à jours
    def on_loop(self) -> None:
        pass
    
    #Calcul des affichages
    def on_render(self, window) -> None:
        pass

