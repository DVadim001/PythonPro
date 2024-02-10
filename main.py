

# Typization
# my_var: int = 100
# stri: str = 'Hello'
# var: list = []


# def my_func(att1: int, att2: int) -> int:
#     return att1*att2
#
# my_func(2,1)


# def calc(a: int, b: int) -> int:
#     return a * b
#
# calc('hello', 25)


# def my_func(attr_1: list) -> int:
#     try:
#         return attr_1.set()
#     except TypeError:
#         if isinstance(attr_1, int):
#             return print(attr_1 * 2)
#     except Exception:
#         if isinstance(attr_1, int):
#             return print(attr_1 * 2)
#             return "All errors of python"
#     finally:
#         print("Adios")
#
# my_func(2)


# m = 34
# spam = "hello"
# summa=None
# try:
#     summa = m + spam
# except AttributeError:
#     pass
#
# print(summa)


# spammer = (10, 12, 234)
# try:
#     spammer.append(678)
# except AttributeError:
#     pass

import logging
logging.debug('Hello, debug!')
logging.info('Hello, info!')
logging.warning('Hello, warning!')
logging.error('Hello, error!')
logging.critical('Hello, critical!')

logging.basicConfig(format='%(name)s | %(levelname)s : %(process)d - %(asctime)s / %(message)s', filename='logs.log')
logging.error('ERRoR!!')


