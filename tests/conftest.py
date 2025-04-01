import pytest

from src.classes import Category, Product


@pytest.fixture
def banana() -> Product:
    return Product("Banan", "Фрукт жёлтого цвета", 100, 125)


@pytest.fixture
def sword() -> Product:
    return Product("Sword", "Меч", 1000, 10)


@pytest.fixture
def katana() -> Product:
    return Product("Katana", "Катана", 2500, 5)


@pytest.fixture
def category_fruits(banana) -> Category:
    return Category("Fruit", "Фрукты", [banana])


@pytest.fixture
def category_weapon(sword, katana) -> Category:
    return Category("Weapon", "Оружия", [sword, katana])

@pytest.fixture
def apple() -> Product:
    return Product("Apple", "Фрукт красного цвета", 120, 100)
