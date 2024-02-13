class Good:

    def __init__(self, name, price, count=1):
        self.name = name
        self.price = price
        self.count = count

    def total_price(self):
        return self.price * self.count

    def show(self):
        return print(f"{self.name:<20}{'{:.2f}'.format(self.price):>7} * {self.count:>3} = {'{:.2f}'.format(self.total_price()):>7}")

