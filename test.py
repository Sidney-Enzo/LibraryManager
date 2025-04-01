from funcoes_secundarias import validar_data, datetime

def test_validar_data() -> None:
    assert not validar_data("invalide date format") 
    assert not validar_data("02-20-2020")
    assert not validar_data("20-12-2008")
    assert validar_data("2000-09-11") == datetime(2000, 9, 11)