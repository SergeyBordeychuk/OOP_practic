def test_init_product(banana):
    assert banana.name == 'Banan'
    assert banana.description == 'Фрукт жёлтого цвета'
    assert banana.price == 100
    assert banana.quantity == 125