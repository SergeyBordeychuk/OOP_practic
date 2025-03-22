import pytest

from src.classes import Product, Category


@pytest.fixture
def product_banan():
    return Product('Banan', 'Фрукт жёлтого цвета', 100, 125)


def test_init_product(product_banan):
    assert product_banan.name == 'Banan'
    assert product_banan.description == 'Фрукт жёлтого цвета'
    assert product_banan.price == 100
    assert product_banan.quantity == 125


@pytest.fixture()
def category_fruits():
    return Category('Fruit', 'Фрукты', [Product('Banan', 'Фрукт жёлтого цвета', 100, 125)])


def test_init_category(category_fruits):
    assert category_fruits.name == 'Fruit'
    assert category_fruits.description == 'Фрукты'
    assert len(category_fruits.products) == 1


@pytest.fixture()
def category_weapon():
    return Category('Weapon', 'Оружия', [Product('Sword', 'Меч', 1000, 10),Product('Katana', 'Катана', 2500, 5)])


def test_counts(category_fruits, category_weapon):
    assert Category.product_count == 4
    assert Category.category_count == 3