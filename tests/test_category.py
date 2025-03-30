from src.classes import Category


def test_init_category(category_fruits):
    assert category_fruits.name == 'Fruit'
    assert category_fruits.description == 'Фрукты'
    assert len(category_fruits.products) == 1


def test_counts(category_fruits, category_weapon):
    assert Category.product_count == 4
    assert Category.category_count == 3


def test_getter(category_fruits, category_weapon):
    assert category_fruits.products == ["Banan, 100 руб. Остаток: 125 шт."]
    assert category_weapon.products == ["Sword, 1000 руб. Остаток: 10 шт.", "Katana, 2500 руб. Остаток: 5 шт."]


def test_add_product(category_fruits, apple):
    category_fruits.add_product(apple)
    assert category_fruits.products == ["Banan, 100 руб. Остаток: 125 шт.", "Apple, 120 руб. Остаток: 100 шт."]
