class DniCharacter:
    character_table = {
        "0":"T",
        "1":"R",
        "2":"W",
        "3":"A",
        "4":"G",
        "5":"M",
        "6":"Y",
        "7":"F",
        "8":"P",
        "9":"D",
        "10":"X",
        "11":"B",
        "12":"N",
        "13":"J",
        "14":"Z",
        "15":"S",
        "16":"Q",
        "17":"V",
        "18":"H",
        "19":"L",
        "20":"C",
        "21":"K",
        "22":"E"
    }
    nie_table = {
        "X":"0",
        "Y":"1",
        "Z":"2"
    }
    @staticmethod
    def nie_converter(dni_object):
        nie_character_value = DniCharacter.nie_table[dni_object.string_dni[0]]
        nie = nie_character_value + dni_object.string_dni[1:]
        return nie
