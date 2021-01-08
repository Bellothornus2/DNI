from .dni_character import DniCharacter
class Dni:

    def __init__(self, string_dni):
        self.string_dni = string_dni
        self.nif_character = None
        self.nif = None

    @property
    def nif_searcher(self):
        index_character_nif = int(self.string_dni)%23
        nif_character = DniCharacter.character_table[str(index_character_nif)]
        self.nif_character = nif_character
        
    @property
    def nif_setter(self):
        if self.nif_character is not None:
            self.nif = self.string_dni + self.nif_character
        else:
            print("No se ha podido asiganr el NIF. ¿Has buscado la letra primero?")