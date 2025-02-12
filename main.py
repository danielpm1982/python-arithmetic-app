# This is a simple arithmetic app created with Python 3 to simply demonstrate its basic syntax.
# For more, read the README.md file below:
# https://github.com/danielpm1982/python-arithmetic-app/blob/master/README.md

from util.algebraic_func.basic_func import BasicFunc as MyMath

class Main:
    def __init__(self):
        # these three variables should be instance variables (not static) so that each instance (user session) would have its own values
        self.input_user_name = None  # stores the user name
        self.input_operation_int = None  # stores which operation to execute on each while iteration
        self.input_operand_string_list = None  # stores a list of strings corresponding to the operand values entered by the user that
                                               # will be processed at each operation

    # this method should be an instance method (not static), so that it can use the "self" reference to its own instance (user session)
    # to get that current user name, exclusively
    def ask_for_input_user_name(self):
        '''
        This instance method asks for the user name and stores it at the input_user_name instance variable
        :return: None
        '''
        self.input_user_name = input("Type your name below:\n").strip().capitalize()

    # this method can be static, as it simply converts an string into an int, and doesn't need to save any value at any
    # instance variable or call any instance method. It's a standalone method, with no instance dependencies
    @staticmethod
    def convert_input_operation_string_to_integer(ios):
        '''
        This class method converts and validates the string number of the operation inserted by the user to the actual
        integer number
        :param ios: the input operation string
        :return: the input operation integer or None if any exception is thrown
        '''
        try:
            return int(ios)
        except ValueError:
            print(f"Error converting string value to integer: \"{ios}\" !")
            return None
        except:
            print("Unknown Exception ! Please try again !")
            return None

    # this method should be an instance method (not static), so that it can use the "self" reference to its own instance (user session)
    # to set that specific user-chosen operation (input_operation_int instance variable)
    def ask_for_input_operation_string_returning_int(self):
        '''
        This class method asks the user to choose an operation to execute by typing the respective string number and
        pressing <ENTER>
        :return: the input operation string converted to an integer or None
        '''
        input_operation_string = input("Please select an operation: 1 - SUM, 2 - SUBTRACTION, 3 - MULTIPLICATION, "
                                       "4 - DIVISION or 5 - EXIT\n(Type one of these numbers and press <ENTER>)\n")
        self.input_operation_int = Main.convert_input_operation_string_to_integer(input_operation_string)
        return self.input_operation_int

    # this method can be static, as it simply converts an string List into an int List, and doesn't need to save any value at any
    # instance variable or call any instance method. It's a standalone method, with no instance dependencies
    @staticmethod
    def convert_input_operand_string_list_to_integer_list(iosl):
        '''
        This class method converts and validates the list of strings of operands inserted by the user to a list of
        corresponding integers
        :param iosl: the input operand string list
        :return: the input operand integer list or None if any exception is thrown
        '''
        split_list = iosl.split(sep=";")
        try:
            return list(map(lambda x: int(x.strip()), split_list))
        except ValueError:
            print(f"Error converting string value to integer: \"{iosl}\" !")
            return None
        except:
            print("Unknown Exception ! Please try again !")
            return None

    # this method should be an instance method (not static), so that it can use the "self" reference to its own instance (user session)
    # to set that specific user-chosen operand list (input_operand_string_list instance variable)
    def ask_for_input_operand_string_list_returning_int_list(self):
        '''
        This instance method asks the user to enter a list of string operand numbers, separated by semicolons - ';' - so that
        the chosen operation can proceed the respective calculations on
        :return: the input operand string list converted to the respective operand integer list or None
        '''
        self.input_operand_string_list = input("Type all numbers to perform the selected operation on, separated by semicolons "
                                          "(;):\n")
        return Main.convert_input_operand_string_list_to_integer_list(self.input_operand_string_list)

    # this method can be static, as it won't depend on other instance variables other than the ones it itself instantiates,
    # namely, the Main() and the MyMath() instances. Instead of using "self", for example, it's gonna use the local variables
    # associated to either these two instances it creates (main or my_math variables). The instance methods above, however,
    # need to be instance methods (not static) in order to have, through the "self" alias, access to the instance of this class
    # when it's instantiated here, at the main() method. In the case of the main() method, it already has full control over
    # the instances it creates - through the local variables that point out to such instances, without depending on any alias
    # (e.g. "self") to access them.
    @staticmethod
    def main():
        '''
        This function initiates the main execution of this class, eventually importing and executing other packages'
        classes as well. This method's interface consists on a while loop through which the user can choose any of the
        arithmetic operations - at each iteration - and insert custom operand numbers in an order that the operators can
        operate on. The available operations are: SUM, SUBTRACTION, MULTIPLICATION, DIVISION and EXIT. The execution
        stops when choosing the operation "5 - EXIT" - or when the program is interrupted by the IDE or keyboard
        interrupting shortcut commands (e.g. Ctrl+C)
        :return: None
        '''
        main = Main() # instantiating the Main class and keeping a local reference to it (at "main" local variable)
        my_math = MyMath() # instantiating the imported BasicFunc class, as MyMath, and keeping a local reference to it (at "my_math" local variable)
        main.ask_for_input_user_name()
        print(f"Hello {main.input_user_name} !")
        while main.input_operation_int != 5:
            main.input_operation_int = main.ask_for_input_operation_string_returning_int()
            match main.input_operation_int:
                case 1:
                    input_operand_int_list = main.ask_for_input_operand_string_list_returning_int_list()
                    if input_operand_int_list:
                        operation_result = my_math.sum(input_operand_int_list)
                        if operation_result:
                            print(f"SUM result of input {main.input_operand_string_list} equals {operation_result} !")
                            print(f"{my_math.log}")
                    continue
                case 2:
                    input_operand_int_list = main.ask_for_input_operand_string_list_returning_int_list()
                    if input_operand_int_list:
                        operation_result = my_math.subtract(input_operand_int_list)
                        if operation_result:
                            print(f"SUBTRACTION result of input {main.input_operand_string_list} equals {operation_result} !")
                            print(f"{my_math.log}")
                    continue
                case 3:
                    input_operand_int_list = main.ask_for_input_operand_string_list_returning_int_list()
                    if input_operand_int_list:
                        operation_result = my_math.multiply(input_operand_int_list)
                        if operation_result:
                            print(f"MULTIPLICATION result of input {main.input_operand_string_list} equals {operation_result} !")
                            print(f"{my_math.log}")
                    continue
                case 4:
                    input_operand_int_list = main.ask_for_input_operand_string_list_returning_int_list()
                    if input_operand_int_list and len(input_operand_int_list) !=2:
                        print("For \"DIVISION\" operation, exactly two input numbers must be passed (not less nor more) !")
                    elif input_operand_int_list:
                        operation_result = my_math.divide(input_operand_int_list)
                        print(f"DIVISION result of input {main.input_operand_string_list} equals {operation_result} !")
                        print(f"{my_math.log}")
                    continue
                case 5:
                    continue
                case _:
                    print(f"Invalid operation number: \"{main.input_operation_int}\" ! Please type a valid integer number for "
                          f"selecting a valid operation !")
        print("\nEND OF EXECUTION !")
        print(f"\nFINAL EXECUTION LOG:\n{my_math.log}")
        print(f"Have a nice day {main.input_user_name} ;D")

# the main() function / method below is only called if this main.py file is being running directly by the interpreter,
# and not by being imported to some other file. In the first case, the dunder variable __name__ will always be set as
# "__main__", while, in the last case, the __name__ would be the str name of this file name, i.e., "main" - or whatever
# other filename (but not exactly "__main__"). This avoids functions / methods being called automatically - e.g. main()
# - when modules / classes are simply importing other modules / classes. After importing any module / class, then, and
# only then, it's up to the programmer to call any function / method from the imported module / class, through the code
# he's writing, not through the import clause itself.
if __name__ == "__main__":
    Main.main()
