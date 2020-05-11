class Person:
    def __init__(self, name: str, phone: str, address: str = None, city: str = None, state: str = None, zip: str = None):
        self.name = name
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self) -> str:
        return f'{self.name}, {self.phone}'


class Driver(Person):
    pass


class Customer(Person):
    pass


class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id


class DeliveryService:
    def add_order(self, order: Order):
        pass

    def cancel_order(self, order_id: int):
        pass

    def complete_order(self, order_id: int):
        pass

    def list_open_orders(self):
        pass

    def list_completed_orders(self):
        pass


if __name__ == '__main__':
    person = Person(name='Bob', phone='555-555-5555')
    driver = Driver(name='Sue', phone='555-555-1234')
    customer = Customer(name='Mary', phone='555-555-9876')

    print(person)
    print(driver)
    print(customer)
