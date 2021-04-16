

class Inventaire(list):
    def __init__(self):
        self._slotInventaire : list = []


if __name__ == "__main__":
    inventaire = Inventaire()
    inventaire.append("youpi")
    print(inventaire)