from decimal import Decimal, getcontext
import random


class Qualean:
    """
    This is a Qualean class inspired by Boolean + Quantum
    concepts.
    """

    def __init__(self, real_state):

        getcontext().prec = 10

        self.real_state = real_state

        if self.real_state not in [1, 0, -1, float(1), float(0), float(-1)]:
            raise ValueError(
                "Input number has to be one of 1, 0, -1, 1.0, 0.0, and -1.0"
            )

        self.real_state = Decimal(str(self.real_state))

        self.imaginary_state = Decimal(str(random.uniform(-1, 1)))

        self.qnum = self.real_state * self.imaginary_state

    def __add__(self, value):
        if type(value) == int:
            return self.qnum + value
        else:
            return self.qnum + value.qnum

    def __eq__(self, value):
        return self.qnum == value.qnum

    def __float__(self):
        return float(self.qnum)

    def __ge__(self, value):
        return self.qnum >= value.qnum

    def __gt__(self, value):
        return self.qnum > value.qnum

    def __le__(self, value):
        return self.qnum <= value.qnum

    def __lt__(self, value):
        return self.qnum < value.qnum

    def __mul__(self, value):
        if type(value) == int:
            return self.qnum * value
        else:
            return self.qnum * value.qnum

    def __invertsign__(self):
        return self.qnum.copy_negate()

#    def __sqrt__(self):
#        return self.qnum.sqrt()

    def __bool__(self):
        return self.qnum != 0

    def __repr__(self):
        return f"{self.qnum}"

    def __str__(self):
        return f"{self.qnum}"

    def __and__(self, value):
        return bool(self.qnum) and bool(value.qnum)

    def __or__(self, value):
        return bool(self.qnum) or bool(value.qnum)



q1 = Qualean(1)
q2 = Qualean(1)

##print(q1, q2)
#print(type(q1), type(q2))
#print(q1.qnum, q2.qnum)
#print(type(q1.qnum), type(q2.qnum))
#
#print(q1.__sqrt__())
#print(Decimal(q1.qnum))
