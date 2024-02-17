import logging

LOG_FORMAT = '%(asctime)s | %(message)s'


def plus(a: int, b: int) -> list:
    try:
        result = a + b
        list_1 = [result]
        return list_1
    except TypeError:
        logging.basicConfig(format=LOG_FORMAT, filename='logs_defPlus.log')


def minus(a: int, b: int) -> list:
    try:
        result = a - b
        list_1 = [result]
        return list_1
    except TypeError:
        logging.basicConfig(format=LOG_FORMAT, filename='logs_defMinus.log')


def multiplication(a: int, b: int) -> list:
    try:
        result = a * b
        list_1 = [result]
        return list_1
    except TypeError:
        logging.basicConfig(format=LOG_FORMAT, filename='logs_defMultiplication.log')
