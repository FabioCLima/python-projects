class FixedFloat:

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"


number = FixedFloat(18.87365)
number2 = FixedFloat.from_sum(19.8789, 21.36987)
print(number2)

money = Euro(18.876)
print(money)

money = Euro.from_sum(18.876, 9.999)
print(money)
