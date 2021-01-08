from .dni_character import DniCharacter
class Dni:

    def __init__(self, string_dni):
        self.string_dni = string_dni
        self.nif_character = None
        self.nif = None
        if string_dni[0] in ["X","Y","Z"]:
            self.is_nie = True
        else:
            self.is_nie = False
        if self.is_nie is True:
            self.nie = DniCharacter.nie_converter(self)
        else:
            self.nie = None
    
    @property
    def nif_searcher(self):
        if self.is_nie is True:
            index_character_nif = int(self.nie)%23
        else:
            index_character_nif = int(self.string_dni)%23
        nif_character = DniCharacter.character_table[str(index_character_nif)]
        self.nif_character = nif_character

    @property
    def nif_setter(self):
        if self.nif_character is not None:
            self.nif = self.string_dni + self.nif_character
        else:
            print("No se ha podido asiganr el NIF. ¿Has buscado la letra primero?")