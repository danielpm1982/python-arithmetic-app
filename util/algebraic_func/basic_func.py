# This is a helper module expected to be imported by a main module that should
# implement a front-end interface, in order that the final user can pass inputs
# and receive outputs, regarding the operations below.

from functools import reduce

def sum(arg_list):
    return reduce(lambda x, y: x + y, arg_list)

def subtract(arg_list):
    return reduce(lambda x, y: x - y, arg_list)

def multiply(arg_list):
    return reduce(lambda x, y: x * y, arg_list)

def divide(arg_list):
    return arg_list[0] / arg_list[1]

# the functions below are for unit testing this module, and should be called through the execute_unit_test() also
# available below, when this module is run directly - and not as an imported module at another module. In this last
# case, only the methods above should be used by the client module. PyTest should be called either from the IDE
# itself (if configured to do so), or manually, at the console prompt, by the tester, by calling
# pytest basic_func.py -v (pytest should be installed first, if not yet installed).

def test_sum():
    try:
        assert sum([1, 2, 3, 4, 5]) == 15
        assert sum([0, 1, 2, 1000000]) == 1000003
        assert sum([-1000000, -2, -1, 0]) == -1000003
        assert sum(([-2, -1, 0, 1, 2])) == 0
    except AssertionError as e:
        print("\nsum(arg_list) failed test !")
        print(e)
        raise e
    else:
        print("\nsum(arg_list) successfully tested - OK !")

def test_subtract():
    try:
        assert subtract([22,5,2]) == 15
        assert subtract([0, 1, 2, 1000000]) == -1000003
        assert subtract([-1000006, -2, -1, 0]) == -1000003
        assert subtract(([-2, -1, -1, 0])) == 0
    except AssertionError as e:
        print("\nsubtract(arg_list) failed test !")
        print(e)
        raise e
    else:
        print("\nsubtract(arg_list) successfully tested - OK !")

def test_multiply():
    try:
        assert multiply([2,5,22]) == 220
        assert multiply([0, 1, 2, 1000000]) == 0
        assert multiply([-1000000, -2, -1, 0]) == 0
        assert multiply(([-2, -1, -1, 2])) == -4
    except AssertionError as e:
        print("\nmultiply(arg_list) failed test !")
        print(e)
        raise e
    else:
        print("\nmultiply(arg_list) successfully tested - OK !")

def test_divide():
    try:
        assert divide([440,2]) == 220
        assert divide([0, 1000000]) == 0
        assert divide([-1000000, -1]) == 1000000
        assert divide(([-2, 440])) == -2/440
    except AssertionError as e:
        print("\ndivide(arg_list) failed test !")
        print(e)
        raise e
    else:
        print("\ndivide(arg_list) successfully tested - OK !")

def execute_unit_test():
    test_sum()
    test_subtract()
    test_multiply()
    test_divide()

if __name__ == "__main__":
    execute_unit_test()
