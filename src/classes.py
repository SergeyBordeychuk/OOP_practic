from abc import ABC


class BaseProduct(ABC):
    name: str
    description: str
    price: int
    quantity: int


class PrintInfoMixin:

    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args} {kwargs}")


class Product(BaseProduct, PrintInfoMixin):
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'


    def __add__(self, other):
        if type(self) == type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            return TypeError


    @classmethod
    def new_product(cls, dictionary):
        return cls(dictionary['name'], dictionary['description'], dictionary['price'], dictionary['quantity'])


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, cost):
        if cost <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            print('Все в порядке')


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    def __str__(self):
        list_products = self.__products
        quantity_products = 0
        for i in list_products:
            quantity_products += i.quantity
        return f'{self.name}, количество продуктов: {quantity_products} шт.'

    @property
    def products(self):
        list_products = self.__products
        list_products_str = []
        for i in list_products:
            list_products_str.append(f'{i.name}, {i.price} руб. Остаток: {i.quantity} шт.')
        return list_products_str


    def add_product(self, product):
        if isinstance(product, Product) or issubclass(product, Product):
            self.__products.append(product)


class Smartphone(Product):
    efficiency: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.color = color
        self.memory = memory
        self.model = model


class LawnGrass(Product):
    country:str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.color = color
        self.germination_period = germination_period
