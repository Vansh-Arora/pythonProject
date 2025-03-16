from random import randint


def generate_array(n, lower_limit, upper_limit):
    return [randint(lower_limit, upper_limit) for i in range(n)]
