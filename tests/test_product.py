from src.classes import Product


def test_init_product(banana):
    assert banana.name == 'Banan'
    assert banana.description == 'Фрукт жёлтого цвета'
    assert banana.price == 100
    assert banana.quantity == 125


def test_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_str_and_add(banana, apple):
    assert str(banana) == 'Banan, 100 руб. Остаток: 125 шт.'
    assert banana + apple == 24500
