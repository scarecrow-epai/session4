import re
import os
import pytest
import inspect
import random
import session4
from decimal import Decimal

state_values = [1, -1, 0]
README_CONTENT_CHECK_FOR = [
    "__and__",
    "__or__",
    "__repr__",
    "__str__",
    "__add__",
    "__eq__",
    "__float__",
    "__ge__",
    "__gt__",
    "__invertsign__",
    "__le__",
    "__lt__",
    "__mul__",
    "__sqrt__",
    "__bool__",
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
    significant indenting."""
    lines = inspect.getsource(session4)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_add():
    for i in range(10):
        q1 = session4.Qualean(random.choice(state_values))
        q2 = session4.Qualean(random.choice(state_values))

        assert q1.__add__(q2) == q1 + q2


def test_equal():
    for i in range(10):
        q1 = session4.Qualean(random.choice(state_values))
        q2 = session4.Qualean(random.choice(state_values))

        assert q1.__eq__(q2) == (q1 == q2)


def test_float():
    for i in range(10):
        q = session4.Qualean(random.choice(state_values))
        assert type(q.__float__()) == float


def test_ge():
    for i in range(10):
        q1 = session4.Qualean(random.choice(state_values))
        q2 = session4.Qualean(random.choice(state_values))

        assert q1.__ge__(q2) == (q1 >= q2)


def test_gt():
    for i in range(10):
        q1 = session4.Qualean(random.choice(state_values))
        q2 = session4.Qualean(random.choice(state_values))

        assert q1.__gt__(q2) == (q1 > q2)


def test_le():
    for i in range(10):
        q1 = session4.Qualean(random.choice(state_values))
        q2 = session4.Qualean(random.choice(state_values))

        assert q1.__le__(q2) == (q1 <= q2)


def test_gt():
    for i in range(10):
        q1 = session4.Qualean(random.choice(state_values))
        q2 = session4.Qualean(random.choice(state_values))

        assert q1.__lt__(q2) == (q1 < q2)


def test_mul():
    for i in range(10):
        q1 = session4.Qualean(random.choice(state_values))
        q2 = session4.Qualean(random.choice(state_values))

        assert q1.__mul__(q2) == q1 * q2


def test_invertsign():
    for i in range(10):
        q = session4.Qualean(random.choice(state_values))
        assert q.__invertsign__() == q.qnum.copy_negate()


def test_sqrt():
   for i in range(10):
       q = session4.Qualean(random.choice(state_values))

       assert q.__sqrt__() == Decimal(q.qnum).sqrt()



def test_bool():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)

    assert q1.__bool__() == True and q2.__bool__() == False and q3.__bool__() == True


def test_hundred_sum():
    q = session4.Qualean(-1)  # random.choice(state_values))
    q_100 = q.qnum * Decimal(100)
    qlist = []
    for i in range(100):
        qlist.append(q.qnum)
    assert sum(qlist) == q_100


def test_million_add():
    q_init = session4.Qualean(0)
    for i in range(1000000):
        q = session4.Qualean(random.choice(state_values))
        q.qnum += q.qnum
    #        q_init.qnum = q_init.qnum + q.qnum
    print(q.qnum)
    assert q.qnum == 0


def test_and():
    q1 = session4.Qualean(0)
    q2 = session4.Qualean(random.choice(state_values))

    assert q1.__and__(q2) == False


def test_or():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(random.choice(state_values))

    assert q1.__or__(q2) == True


def test_super_and():
    q1 = session4.Qualean(0)

    assert q1.__and__(q2) == False


def test_super_or():
    q1 = session4.Qualean(1)

    assert q1.__or__(q2) == True



def test_correct_init():
	with pytest.raises(ValueError):
		q = session4.Qualean(0.5)


def test_qualean_object_range():
	for i in range(100):
		q = session4.Qualean(random.choice(state_values))
		assert q.qnum < 1 and q.qnum > -1


def test_value_at_zero():
	for i in range(100):
		q = session4.Qualean(0)
		assert q.qnum == 0

