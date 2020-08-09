from decimal import Decimal, getcontext
import random
import cmath

getcontext().prec = 10


class Qualean:
    """
    This is a Qualean class inspired by Boolean + Quantum
    concepts.
    """

    def __init__(self, real_state):

        self.real_state = real_state

        if self.real_state not in [1, 0, -1, float(1), float(0), float(-1)]:
            raise ValueError(
                "Input number has to be one of 1, 0, -1, 1.0, 0.0, and -1.0"
            )

        self.real_state = Decimal(str(self.real_state))

        self.imaginary_state = Decimal(str(random.uniform(-1, 1)))

        self.qnum = self.real_state * self.imaginary_state

    def __add__(self, value):
        if isinstance(value, Qualean):
            return self.qnum + value.qnum
        else:
            return self.qnum + value

    def __eq__(self, value):
        if isinstance(value, Qualean):
            return self.qnum == value.qnum
        else:
            return self.qnum == value

    def __float__(self):
        return float(self.qnum)

    def __ge__(self, value):
        if isinstance(value, Qualean):
            return self.qnum >= value.qnum
        else:
            return self.qnum >= value

    def __gt__(self, value):
        if isinstance(value, Qualean):
            return self.qnum > value.qnum
        else:
            return self.qnum > value

    def __le__(self, value):
        if isinstance(value, Qualean):
            return self.qnum <= value.qnum
        else:
            return self.qnum <= value

    def __lt__(self, value):
        if isinstance(value, Qualean):
            return self.qnum < value.qnum
        else:
            return self.qnum < value

    def __mul__(self, value):
        if isinstance(value, Qualean):
            return self.qnum * value.qnum
        else:
            return self.qnum * value

    def __invertsign__(self):
        return self.qnum.copy_negate()

    def __sqrt__(self):
        if self.qnum > 0:
            return self.qnum.sqrt()
        else:
            return cmath.sqrt(self.qnum)

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
