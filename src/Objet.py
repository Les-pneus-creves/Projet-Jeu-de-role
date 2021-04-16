

class Objet:
    def __init__(self, nom: string, image, stackable: int):
        self._nom = nom
        self._image = image
        self._stackable = stackable

    def getImage(self):
        return self.__image