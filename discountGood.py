from good import Good


class DiscountGood(Good):
    def __init__(self, name, price, count=1, discount=None):
        super().__init__(name, price, count)
        self.discount = discount

    def total_price(self):
        return (self.price * self.count) - round(self.price * (self.discount/100))

    def show(self):
        return print(f"{self.name:<20}{'{:.2f}'.format(self.price):>7} * {self.count:>3} = {'{:.2f}'.format(self.total_price()):>7} (-{self.discount}%)")






