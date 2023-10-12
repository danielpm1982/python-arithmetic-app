# This is a simple arithmetic app created with Python 3 to simply demonstrate its basic syntax.
# For more, read the README.md file below:
# https://github.com/danielpm1982/python-arithmetic-app/blob/master/README.md

# different ways of importing modules in Python (either python packages or python files). Adjust the use according to
# what method you choose below. Specifically, if you declare an alias, use it, otherwise, don't. Whatever comes on
# the right side of the "import" keyword must be called explicitly at the code (maybe not only the function name),
# while what comes between "from" and "import" (inner packages) must not and is implicitly considered at the code:
# from util.algebraic_func.basic_func import *
# from util.algebraic_func.basic_func import sum, subtract, multiply, divide
# import util.algebraic_func.basic_func as my_math
# the statement below imports the whole basic_func module (and its functions) from the packages util.algebraic_func,
# setting "my_math' as an alias to the basic_func module
from util.algebraic_func import basic_func as my_math

# global variables used inside functions
input_user_name = None # stores the user name
input_operation_int = None # stores which operation to execute on each while iteration
input_operand_string_list = None # stores a list of strings corresponding to the operand values entered by the user that
                                 # will be processed at each operation


def ask_for_input_user_name():
    '''
    This function asks for the user name and stores it at the input_user_name global variable
    :return: None
    '''
    global input_user_name
    input_user_name = input("Type your name below:\n")


def convert_input_operation_string_to_integer(ios):
    '''
    This function converts and validates the string number of the operation inserted by the user to the actual
    integer number
    :param ios: the input operation string
    :return: the input operation integer or None if any exception is thrown
    '''
    try:
        input_operation_integer = int(ios)
        return input_operation_integer
    except ValueError:
        print(f"Error converting string value to integer: \"{ios}\" !")
        return None
    except:
        print("Unknown Exception ! Please try again !")
        return None


def ask_for_input_operation_string_returning_int():
    '''
    This function asks the user to choose an operation to execute by typing the respective string number and pressing <ENTER>
    :return: the input operation string converted to an integer or None
    '''
    input_operation_string = input("Please select an operation: 1 - SUM, 2 - SUBTRACTION, 3 - MULTIPLICATION, "
                                   "4 - DIVISION or 5 - EXIT\n(Type one of these numbers and press <ENTER>)\n")
    return convert_input_operation_string_to_integer(input_operation_string)


def convert_input_operand_string_list_to_integer_list(iosl):
    '''
    This function converts and validates the list of strings of operands inserted by the user to a list of
    corresponding integers
    :param iosl: the input operand string list
    :return: the input operand integer list or None if any exception is thrown
    '''
    split_list = iosl.split(sep=";")
    try:
        input_operand_integer_list = list(map(lambda x: int(x.strip()), split_list))
        return input_operand_integer_list
    except ValueError:
        print(f"Error converting string value to integer: \"{iosl}\" !")
        return None
    except:
        print("Unknown Exception ! Please try again !")
        return None


def ask_for_input_operand_string_list_returning_int_list():
    '''
    This function asks the user to enter a list of string operand numbers, separated by semicolons - ';' - so that
    the chosen operation can proceed the respective calculations on
    :return: the input operand string list converted to the respective operand integer list or None
    '''
    global input_operand_string_list
    input_operand_string_list = input("Type all numbers to perform the selected operation on, separated by semicolons "
                                      "(;):\n")
    return convert_input_operand_string_list_to_integer_list(input_operand_string_list)


def main():
    '''
    This function initiates the main execution of this module, eventually importing and executing other modules'
    functions as well. This module's interface consists on a while loop through which the user can choose any of the
    arithmetic operations - at each iteration - and insert custom operand numbers in an order that the operators can
    operate on. The available operations are: SUM, SUBTRACTION, MULTIPLICATION, DIVISION and EXIT. The execution
    stops when choosing the operation "5 - EXIT" - or when the program is interrupted by the IDE or keyboard
    interrupting shortcut commands (e.g. Ctrl+C)
    :return: None
    '''
    ask_for_input_user_name()
    print(f"Hello {input_user_name} !")
    global input_operation_int
    while input_operation_int != 5:
        input_operation_int = ask_for_input_operation_string_returning_int()
        match input_operation_int:
            case 1:
                input_operand_int_list = ask_for_input_operand_string_list_returning_int_list()
                if input_operand_int_list:
                    operation_result = my_math.sum(input_operand_int_list)
                    if operation_result:
                        print(f"SUM result of input {input_operand_string_list} equals {operation_result} !")
                continue
            case 2:
                input_operand_int_list = ask_for_input_operand_string_list_returning_int_list()
                if input_operand_int_list:
                    operation_result = my_math.subtract(input_operand_int_list)
                    if operation_result:
                        print(f"SUBTRACTION result of input {input_operand_string_list} equals {operation_result} !")
                continue
            case 3:
                input_operand_int_list = ask_for_input_operand_string_list_returning_int_list()
                if input_operand_int_list:
                    operation_result = my_math.multiply(input_operand_int_list)
                    if operation_result:
                        print(f"MULTIPLICATION result of input {input_operand_string_list} equals {operation_result} !")
                continue
            case 4:
                input_operand_int_list = ask_for_input_operand_string_list_returning_int_list()
                if input_operand_int_list and len(input_operand_int_list) !=2:
                    print("For \"DIVISION\" operation, exactly two input numbers must be passed (not less nor more) !")
                elif input_operand_int_list:
                    operation_result = my_math.divide(input_operand_int_list)
                    print(f"DIVISION result of input {input_operand_string_list} equals {operation_result} !")
                continue
            case 5:
                continue
            case _:
                print(f"Invalid operation number: \"{input_operation_int}\" ! Please type a valid integer number for "
                      f"selecting a valid operation !")
    print("\nEND OF EXECUTION !")
    print(f"Have a nice day {input_user_name} ;D")

# the main() function / method below is only called if this main.py file is being running directly by the interpreter,
# and not by being imported to some other file. In the first case, the dunder variable __name__ will always be set as
# "__main__", while, in the last case, the __name__ would be the str name of this file name, i.e., "main" - or whatever
# other filename (but not exactly "__main__"). This avoids functions / methods being called automatically - e.g. main()
# - when modules / classes are simply importing other modules / classes. After importing any module / class, then, and
# only then, it's up to the programmer to call any function / method from the imported module / class, through the code
# he's writing, not through the import clause itself.
if __name__ == "__main__":
    main()
