
class Objet:
    def __init__(self, nom: str, image, stackable: int):
        self._nom = nom
        self._image = image
        self._stackable = stackable

    def __str__(self):
        return "[" + self._nom + ", max= " + str(self._stackable) + "]"

    def getImage(self):
        return self._image

    def getNom(self) -> str:
        return self._nom

    def getStackable(self) -> int:
        return self._stackable
