from good import Good
from discountGood import DiscountGood


class Cart:
    def __init__(self, goods):
        self.goods = goods

    def total_price(self):
        sum_total = 0
        for i in self.goods:
            sum_total += i.total_price()
        return sum_total

    def show_check(self):
        print(f'{"Name":<20}{"PPU":>7} {"CNT":>5} {"Price":>9}  {"Disc":>3}.\n{"=" * 50}')
        for i in self.goods:
            i.show()
        print(f"{'=' * 50}\n{'Total':<33} = {'{:.2f}'.format(self.total_price()):>7}")


cart = Cart([Good('Bread', 17, 3), Good('Water', 19, 2), DiscountGood('Juice', 80, 1, 20), Good('Toilet Paper', 19, 10), Good('Coca-Cola', 1)])

cart.show_check()
