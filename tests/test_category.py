from src.classes import Category


def test_init_category(category_fruits):
    assert category_fruits.name == 'Fruit'
    assert category_fruits.description == 'Фрукты'
    assert len(category_fruits.products) == 1


def test_counts(category_fruits, category_weapon):
    assert Category.product_count == 4
    assert Category.category_count == 3