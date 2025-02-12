# This class basically creates a SimpleLogger instance, which uses python properties (decorators) for getting and
# setting the log itself, which is simply a str, initialized with an initial line of text, with the current datetime
# at the Logger object creation, later appended with additional lines of text, entered by the user, concatenated each
# line with the actual datetime of when each line is added. This class can be inherited or imported by the BasicFunc
# class, in order to log each input and output of such operator methods. Some OO programming structures are exemplified
# here, including __init__ instance initializers (__new__ is managed automatically), instance methods, static methods
# and decorators for properties, instead of traditional getter and setter methods. In this last case, instead of calling
# traditional accessor methods, one should use the mapped property as a simple attribute, either for getting its value,
# as for assigning a new value to it - you do not call the properties' getter or setter methods directly, as the
# properties are already mapped to them. The name of both the getter and setter methods must be the same, which will
# also be the name of the property - in this case: "log".

from datetime import datetime

class SimpleLogger:
    def __init__(self):
        self._log = SimpleLogger._get_new_log()

    @property
    def log(self):
        return self._log+"\nEnd of this log !\n"

    @log.setter
    def log(self, text):
        self._log += f"\n{datetime.now().isoformat()}: {text}"

    def clear_log(self):
        self._log = SimpleLogger._get_new_log()

    @staticmethod
    def _get_new_log():
        return "Custom Log - danielpm1982.com. Created at: " + datetime.now().isoformat()
