# This is a helper class expected to be imported by a main module or class that
# should implement a front-end interface, in order that the final user can pass
# inputs and receive outputs, regarding the operations below. This class inherits
# from the SimpleLogger class, in order to log in memory all inputs and outputs
# of each operation. It also could simply import SimpleLogger and use it as a
# standalone class as well - this is just an example of how to implement inheritance
# in Python. All properties, attributes and methods from the inherited parent class
# are then accessible through the "self" of the inheriting class. You only need to
# refer to the super() at the initializer, not at each method or property call. In
# this use case, as log is a property of an instance of the inherited class, all
# operation methods are also declared as instance methods and not class methods
# (static). A same instance of the inherited class should be used for all methods,
# so that we register all operations into one same log.

from functools import reduce
from util.algebraic_func.simple_logger import SimpleLogger

class BasicFunc(SimpleLogger):
    def __init__(self):
        super().__init__()

    def sum(self, arg_list):
        result = reduce(lambda x, y: x + y, arg_list)
        self.log = "operation: addition | arguments list: "+BasicFunc.get_stringuified_list(arg_list)+" | result: "+str(result)
        return result

    def subtract(self, arg_list):
        result = reduce(lambda x, y: x - y, arg_list)
        self.log = "operation: subtraction | arguments list: "+BasicFunc.get_stringuified_list(arg_list)+" | result: "+str(result)
        return result

    def multiply(self, arg_list):
        result = reduce(lambda x, y: x * y, arg_list)
        self.log = "operation: multiplication | arguments list: "+BasicFunc.get_stringuified_list(arg_list)+" | result: "+str(result)
        return result

    def divide(self, arg_list):
        result = arg_list[0] / arg_list[1]
        self.log = "operation: division | arguments list: "+BasicFunc.get_stringuified_list(arg_list)+" result: | "+str(result)
        return result

    @staticmethod
    def get_stringuified_list(e_list):
        result_string_with_final_comma = "".join(map(lambda e: str(e) + ",", e_list))
        result_string = result_string_with_final_comma[0:len(result_string_with_final_comma) - 1]
        return result_string

# the methods below are for unit testing this class, and should be called through the execute_unit_test(), also
# available below, when this class is run directly - and not as an imported class at another module. In this last
# case, only the methods above should be used by the client class. PyTest should be called either by the IDE
# itself (if configured to do so), or manually, at the console prompt, by the tester, by calling
# pytest basic_func.py -v (pytest should be installed first, if not yet installed).

# one same instance of BasicFunc class - and therefore of the parent SimpleLogger class - should be used for calling
# all operations through it, in order to register these operations into one same log property. Both here, at the unit
# testing, as at the front-end class that's gonna import and use this BasicFunc class for the final user.
basic_func = BasicFunc()
def test_sum():
    global basic_func
    try:
        assert basic_func.sum([1, 2, 3, 4, 5]) == 15
        assert basic_func.sum([0, 1, 2, 1000000]) == 1000003
        assert basic_func.sum([-1000000, -2, -1, 0]) == -1000003
        assert basic_func.sum(([-2, -1, 0, 1, 2])) == 0
    except AssertionError as e:
        print("\nsum(arg_list) failed test !")
        print(e)
        raise e
    else:
        print(f"\n{basic_func.log}")
        print("\nsum(arg_list) successfully tested - OK !")

def test_subtract():
    global basic_func
    try:
        assert basic_func.subtract([22,5,2]) == 15
        assert basic_func.subtract([0, 1, 2, 1000000]) == -1000003
        assert basic_func.subtract([-1000006, -2, -1, 0]) == -1000003
        assert basic_func.subtract(([-2, -1, -1, 0])) == 0
    except AssertionError as e:
        print("\nsubtract(arg_list) failed test !")
        print(e)
        raise e
    else:
        print(f"\n{basic_func.log}")
        print("\nsubtract(arg_list) successfully tested - OK !")

def test_multiply():
    global basic_func
    try:
        assert basic_func.multiply([2,5,22]) == 220
        assert basic_func.multiply([0, 1, 2, 1000000]) == 0
        assert basic_func.multiply([-1000000, -2, -1, 0]) == 0
        assert basic_func.multiply(([-2, -1, -1, 2])) == -4
    except AssertionError as e:
        print("\nmultiply(arg_list) failed test !")
        print(e)
        raise e
    else:
        print(f"\n{basic_func.log}")
        print("\nmultiply(arg_list) successfully tested - OK !")

def test_divide():
    global basic_func
    try:
        assert basic_func.divide([440,2]) == 220
        assert basic_func.divide([0, 1000000]) == 0
        assert basic_func.divide([-1000000, -1]) == 1000000
        assert basic_func.divide(([-2, 440])) == -2/440
    except AssertionError as e:
        print("\ndivide(arg_list) failed test !")
        print(e)
        raise e
    else:
        print(f"\n{basic_func.log}")
        print("\ndivide(arg_list) successfully tested - OK !")

def execute_unit_test():
    test_sum()
    test_subtract()
    test_multiply()
    test_divide()

if __name__ == "__main__":
    execute_unit_test()
