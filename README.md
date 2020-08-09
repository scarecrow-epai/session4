# Session 4


This is the README for session4 - Numerics Part 2.


This file contains information present in `session4.py` file and the test cases in `test_session4.py`.


## session4.py

The functions are - 


```
class Qualean:
    """
    This is a Qualean class inspired by Boolean + Quantum
    concepts.
    """
```
The state is set using a real number (-1, 0, 1). This number is then multiplied with a random 
number sampled from a unifrorm distribution.

### __add__()

This method adds two objects.

### __eq__()

This method return a bool be comparing 2 objects. If equal, `True` is returned. Else, `False`. 

### ___float__()
This method converts Qualean object to float.


### __ge__()
This mehtod compares if a Qualean object is greater than or equal to another object.

### __gt__()
This method compares if a Qualean object is greater than another object.

### __le__(self, value):
This method compares if a Qualean object is less than or equal to  another object.

### __lt__()
This method compares if a Qualean object is less than another object.

### __mul__()
This method multiplies 2 Qualean objects.

### __invertsign__()
Inverts the sign of a Qualean object.


###  __sqrt__()
Calculate aquare root of a qualean object.

### __bool__()
Calculate boolean value of a qualean object.

### __repr__()
Repr of class.


### __str__()
Str of class. 

### __and__()
`and` bool implementation for 2 objects.

### __or__()
`or` bool implementation for 2 objects.





## Test Functions

Following section explains all the test methods used. 


### test_readme_exists():
Checks if README exists.

### test_readme_contents():
Check if README.md file is interesting! Should have atleast 500 words.


### test_readme_proper_description()
Describe all the functions/class well in your README.md file.


### test_readme_file_for_formatting():
README has atleast 10 "#".

### test_indentations():
Code indentation should follow PEP8 guidelines.


### test_function_name_had_cap_letter():
No Capital letter(s) in your function names.


### test_add():
Test add function.

### test_equal():
Test equaal function.

### test_float():
Test float function.

### test_ge():
Test greater than or equal to function.

### test_gt():
Test greater than function.


### test_le():
Test less than or equal to function.


### test_gt():
Test less than function.

### test_mul():
Test multiplication function.


### test_invertsign():
Test inversion function.


### test_sqrt():
Test inversion function.
        
### test_bool():
Test bool function.


### test_hundred_sum():
Test hundre sum function. q + q + q ... 100 times = 100 * q.

### test_million_add():
Test million add function. isum of 1 million different qs is very close to zero (use isclose).


### test_and():
Test and function.

### test_or():
Test or function.

### test_super_and():
q1 and q2 returns False when q2 is not defined as well and q1 is False

### test_super_or():
q1 or q2 returns True when q2 is not defined as well and q1 is not false

### test_correct_init():
Raises ValueError on incorrect init.


### test_qualean_object_range():
Qualean should lie between (-1, 1).

### test_value_at_zero():
Qualean value at state 0 should be zero.
