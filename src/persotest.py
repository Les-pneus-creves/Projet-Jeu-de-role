class persotest:

    def __init__(self, name, vie, degat):
        self._name = name
        self._vie = vie
        self._degat = degat
        self._estVivant = True

    def getName(self):
        return self._name

    def getVie(self):
        return self._vie

    def getDegat(self):
        return self._degat

    def setVie(self, int):
        self._vie = int
        if self._vie < 0 :
            self._estVivant = False
            return " ce qui le tue lol"
        else:
            return ""

    def faireDegat(self, inte, cible):
        temp = cible.setVie(cible.getVie() - inte)
        return self._name + " inflige " +  str(inte) + " dégats à " + cible.getName() + " "+ temp + " il lui reste " + str(cible.getVie()) + " pdv"

    def getVivant(self):
        return self._estVivant

    