# Проект OOP

## ## Описание:

Проект OOP - это проект практика Объектно-Ориентированного Программирования

## Установка:

1. Клонируйте репозиторий:
```commandline
git clone https://github.com/SergeyBordeychuk/OOP_practic.git
```
2. Установите зависимости:
```commandline
pip install -r requirements.txt
```

## Тестирование:

Тесты проведены для всех функций с помощью:
1. Фисктуры
2. Параметризации

Все тесты находятся в пакете tests

### Модуль classes:
1. Класс Product -> принимает name, description, price и quantity
2. Класс Category -> принимает name, description, products
3. Дочерний класс Smartphone(Product) -> принимает name, description, price, quantity, color, model, memory и efficiency
4. Дочерний класс LawnGrass(Product) -> принимает name, description, price, quantity, color, country и germination_period