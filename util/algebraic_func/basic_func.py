from functools import reduce


def sum(arg_list):
    return reduce(lambda x, y: x + y, arg_list)

def subtract(arg_list):
    return reduce(lambda x, y: x - y, arg_list)

def multiply(arg_list):
    return reduce(lambda x, y: x * y, arg_list)


def divide(arg_list):
    return arg_list[0] / arg_list[1]
