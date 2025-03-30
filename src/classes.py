class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


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
