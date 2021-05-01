from Slot_inventaire import Slot_inventaire
from Objet import Objet


class Inventaire(list):

    def __init__(self, nbArme, nbEquipement, nbRessources):
        """ En faite se serais plus pour l'inventaire personnage toutes ces spécificité.
            Pour l'inventaire de base on ferais des slots capables d'accueillir tout types d'objets (les coffres)"""
        super(Inventaire, self).__init__()
        for i in range(nbArme):
            self.append(Slot_inventaire("Arme"))
        for i in range(nbEquipement):
            self.append(Slot_inventaire("Equipement"))
        for i in range(nbRessources):
            self.append(Slot_inventaire("Ressources"))

    def append(self, slot: Slot_inventaire):
        """Overload de la méthode append des list, cela permet d'ajouter que des Slot_inventaire à notre Inventaire"""
        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).append(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def insert(self, index, slot: Slot_inventaire):
        """ Overload de la méthode insert des list, cela permet d'ajouter que des Slot_inventaire à notre Inventaire
            Pas forcément utile mais pour que se soit jolie"""
        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).insert(index, slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def __add__(self, slot: Slot_inventaire):
        """ Overload de l'opérateur +, cela permet d'ajouter que des Slot_inventaire à notre Inventaire
            Pas forcément utile mais pour que se soit jolie"""
        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).__add__(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def __iadd__(self, slot: Slot_inventaire):
        """ Overload de l'opérateur +=, cela permet d'ajouter que des Slot_inventaire à notre Inventaire
            Pas forcément utile mais pour que se soit jolie"""
        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).__iadd__(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def __str__(self):
        retour = "["
        i = 0
        for slot in self:
            retour += str(slot)
            if i < len(self) - 1:
                retour += ", "
                i += 1
        retour += "]"
        return retour

    def contientObjet(self, objet: Objet):
        i = 0
        for slot in self:
            slotObjet = slot.getObjet()
            if slotObjet is not None:
                if slotObjet.getNom() == objet.getNom():
                    return i
            i += 1
        return -1

    def ajouter(self, objet: Objet, nombre=1):
        position = self.contientObjet(objet)
        if position != -1 and not self[position].plein():
            ajout = self[position].ajouter(nombre)
            if ajout > 0:
                self.ajouter(objet, ajout)
                return
            elif ajout == 0:
                return
        else:
            for slot in self:
                ajout = slot.ajouter(objet, nombre)
                if ajout == 0:
                    break
                elif ajout == -1:
                    continue
                else:
                    self.ajouter(objet, ajout)
                    return



if __name__ == "__main__":
    inventaire = Inventaire(1, 1, 5)
    inventaire.ajouter(Objet("Ressources_Patate", "prout", 3), 5)
    inventaire.ajouter(Objet("Ressources_Oignons", "prout", 4), 5)
    inventaire.ajouter(Objet("Arme_Fusil", "prout", 1), 2)
    print(inventaire)
