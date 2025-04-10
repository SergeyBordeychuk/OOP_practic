import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


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

@pytest.fixture
def iphon() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def blue_grass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Синяя")
