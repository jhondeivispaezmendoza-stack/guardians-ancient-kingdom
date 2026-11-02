from personajes import Guerrero, Mago, Arquero, Combate
def test_guerrero():
    assert Guerrero("G",100,20,5).atacar(Guerrero("O",100,10,10)) == 14
def test_mago():
    assert Mago("M",100,30,5).atacar(Guerrero("O",100,10,100)) == 30
def test_arquero():
    assert Arquero("A",100,25,10).atacar(Guerrero("O",100,10,10)) == 30
def test_combate():
    assert Combate(Guerrero("G",50,20,5), Mago("M",50,20,5)).iniciar() is not None
def test_empate():
    assert "Empate" in Combate(Arquero("A1",50,5,20), Arquero("A2",50,5,20)).iniciar()
