from  src.dni import Dni

def test_general():
    dni = Dni("12345678")
    dni.nif_searcher
    dni.nif_setter
    assert dni.nif == "12345678Z"

def test_nie():
    dni = Dni("Y1234567")
    dni.nif_searcher
    dni.nif_setter
    assert dni.nif == "Y1234567X"

def test_nie_x_character():
    dni = Dni("X1234567")
    dni.nif_searcher
    dni.nif_setter
    assert dni.nif == "X1234567L"