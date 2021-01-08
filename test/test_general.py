from  src.dni import Dni

def test_general():
    dni = Dni("12345678")
    dni.nif_searcher
    dni.nif_setter
    assert dni.nif == "12345678Z"