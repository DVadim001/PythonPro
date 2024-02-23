# # Typization
# # my_var: int = 100
# # stri: str = 'Hello'
# # var: list = []
#
#
# # def my_func(att1: int, att2: int) -> int:
# #     return att1*att2
# #
# # my_func(2,1)
#
#
# # def calc(a: int, b: int) -> int:
# #     return a * b
# #
# # calc('hello', 25)
#
#
# # def my_func(attr_1: list) -> int:
# #     try:
# #         return attr_1.set()
# #     except TypeError:
# #         if isinstance(attr_1, int):
# #             return print(attr_1 * 2)
# #     except Exception:
# #         if isinstance(attr_1, int):
# #             return print(attr_1 * 2)
# #             return "All errors of python"
# #     finally:
# #         print("Adios")
# #
# # my_func(2)
#
#
# # m = 34
# # spam = "hello"
# # summa=None
# # try:
# #     summa = m + spam
# # except AttributeError:
# #     pass
# #
# # print(summa)
#
#
# # spammer = (10, 12, 234)
# # try:
# #     spammer.append(678)
# # except AttributeError:
# #     pass
#
# import logging
#
#
# # logging.debug('Hello, debug!')
# # logging.info('Hello, info!')
# # logging.warning('Hello, warning!')
# # logging.error('Hello, error!')
# # logging.critical('Hello, critical!')
#
# # logging.basicConfig(format='%(name)s | %(levelname)s : %(process)d - %(asctime)s / %(message)s',
# #                     filename='logs.log',
# #                     filemode='a',
# #                     level=logging.INFO,
# #                     datefmt='%Y:%M:%D %H:%M')
# # logging.info('inf')
#
#
# # Validation
#
# # import typing
# # def func(player: typing.List[int], player_2: typing.Union[str, int]):
# #     pass
# #
# # func()
#
# # from typing import List, Dict
# #
# # from pydantic import BaseModel
# #
# # class Player(BaseModel):
# #     player_name: str
# #     player_deposit: int
# #     player_items: List[Dict[str, int]]
# #     player_friends: List[str] = ['Jordan']
# #
# #
# # player_1 = Player(player_name='Micael', player_deposit=100_000, player_items=[{'key':0}])
# # print(player_1)
#
#
# # from pydantic import BaseModel
# #
# #
# # class Posts(BaseModel):
# #     user: str
# #     comment: str
# #     likes: int=0
# #
# #
# # input_dict = {'user': 'two', 'comment': 'super', 'likes': 5}
# #
# # post1 = Posts(user='one', comment='klass', likes=3)
# # post2 = Posts(**input_dict)
# #
# # print(post1.user)
# # print(post2)
#
#
# # from pydantic import BaseModel
# # class Client(BaseModel):
# #     name: str
# #     number:int
# #     mail: str
# #
# # class Bank(BaseModel):
# #     client: Client
# #     money_amount: int
# #     currency: str
# #
# # client_1 = Client(name="Jordan", number=100_000, mail='test@test.com')
# #
# # bank_1 = Bank(client=client_1, money_amount=100, currency='sum')
# # print(bank_1)
# # print(bank_1.client.name)
#
#
# # from pydantic import BaseModel
# # class Users(BaseModel):
# #     name: str
# #     followers: int
# #     posts: int
# #
# # class Comments(BaseModel):
# #     user: User
# #     comment: str
# #     likes: int=0
# #
# # user_1 = Users(name='Pavel', followers=10, posts=5)
# # comment_1 = Comments(user=user_1, comment='plus', likes=3)
#
#
# # from pydantic import BaseModel
# # class User(BaseModel):
# #     username: str
# #     mail: str
# #     language: str
# #
# # class Artist(BaseModel):
# #     artist_name: str
# #     artist_followers: int
# #
# # class Song(BaseModel):
# #     artist: Artist
# #     song_name: str
# #     date_of_publishing: str
# #
# # class Playlist(BaseModel):
# #     user: User
# #     song: Song
# #     likes: int
# #
# # user_1 = User(username='one', mail='test@test.com', language='rus')
# # artist_1 = Artist(artist_name='Pevets', artist_followers=100_000)
# # song_1 = Song(artist=artist_1, song_name='Pesnya', date_of_publishing='vchera')
# # playlist_1 = Playlist(user=user_1, song=song_1, likes=1)
# #
# # print(playlist_1.song.artist.artist_name)
#
#
# # Потоки
#
#
# # from threading import Thread
# # def show_products(products):
# #     for i in products:
# #         print(f"{i} \nPrice: $20")
# #
# # all_prod= ['Apple', 'Bread', 'Burger']
# # t1 = Thread(target=show_products, args=(all_prod,))
# #
# # t1.start()
# # print('Hello')
#
#
# # from threading import Thread
# # def send_message(users) -> None:
# #     for i in users:
# #         print(f"{i} \n")
# # users_list: list = ['Jordan', 'Pasha', 'Mikle']
# # t1: Thread = Thread(target=send_message, args=(users_list,))
# # t1.start()
# # print('Hello potok world')
#
#
# # Generators
#
# # def check_queue(clients)->str:
# #     for client in clients:
# #         yield client
# #
# # all_clients:list = ['Pasha', 'Jordan', 'Vika']
# # hospital: str = check_queue(all_clients)
# # print(next(hospital))
# # print(next(hospital))
# # print(next(hospital))
#
#
# # def weeks(days) -> str:
# #     for day in days:
# #         yield day
# #
# #
# # days: list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
# # a: str = weeks(days)
# # try:
# #     print(next(a))
# #     print(next(a))
# #     print(next(a))
# #     print(next(a))
# #     print(next(a))
# #     print(next(a))
# #     print(next(a))
# #     print(next(a))
# #     print(next(a))
# # except StopIteration:
# #     print('Конец!!!')
#
#
#
#
# # import asyncio
# # import time
# # async def task_1():
# #     await asyncio.sleep(2)
# #     print("Hello async function")
# #
# # async def task_2():
# #     print('task2')
# # async def main():
# #     t1 = asyncio.create_task(task_1())
# #     t2 = asyncio.create_task(task_2())
# #     await t1
# #     await t2
# #
# # asyncio.run(main())
#
#
# # import asyncio
# # users_list: list = ['Jordan', 'Pasha', 'Mikle']
# #
# #
# # async def send_massages(users: list) -> None:
# #     for i in users:
# #         print(f'Hello, {i}')
# #
# #
# # async def collect():
# #     u = asyncio.create_task(send_massages(users_list))
# #     await u
# #
# # asyncio.run(collect())
#
#
#
# # import asyncio
# #
# # async def menu(i:int) -> None:
# #     print(f'Async func {i} open')
# #     await asyncio.sleep(2)
# #     print(f'Async func {i} CLOSE')
# #
# # async def main():
# #     async_list = []
# #     for i in range(10):
# #         t1 = asyncio.create_task(menu(i))
# #         async_list.append(t1)
# #
# #     await asyncio.gather(*async_list)
# #
# #     print('END')
#
#
#
#
# # AIOHTTP
#
# import aiohttp
# import asyncio
# import requests
# from bs4 import BeautifulSoup
# import time
#
# url = 'http://quotes.toscrape.com/'
#
#
# async def web_async_parce(page: int) -> None:
#     all_quotes = []
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f'{url}/page/{page}/') as response:
#             web_content = await response.text()
#             bs_content = BeautifulSoup(web_content, 'html.parser')
#             finder = bs_content.findAll('span', {'itemprop': 'text'})
#             for quote in finder:
#                 all_quotes.append(quote.text)
#     print(f'Все {len(all_quotes)} цитат скачаны, на странице {page}')
#     print(all_quotes)
#
#
#
# async def main_async():
#     start_time = time.time()
#     my_list = []
#
#     for i in range(1, 11):
#         task = asyncio.create_task(web_async_parce(i))
#         my_list.append(task)
#
#     await asyncio.gather(*my_list)
#
#     end_time = time.time() - start_time
#     print(f'Асинхронный код спарсил все страницы зв {end_time:.2f}')
#
#
# asyncio.run(main_async())






# Testing, Unit-тесты


# def check_positive_numbers(x: int, y: int) -> int | float:
#     assert x > 0 and y > 0, 'Число отрацательное'
#     return x * y
#
#
# print(check_positive_numbers(23,89))
# print(check_positive_numbers(-10, -189))
# print(check_positive_numbers(10, 35))



# def check_positive_numbers(x: int, y: int) -> int | float:
#     assert x > 0 or y < 0, 'Число отрацательное'
#     return x * y
#
#
# print(check_positive_numbers(23,89))
# print(check_positive_numbers(-10, -189))
# print(check_positive_numbers(10, 35))



# def check_positive_numbers(x: int, y: int) -> int | float:
#     """
#     >>> check_positive_numbers(2, 4)
#     8
#
#     >>> check_positive_numbers(2, {'key': 'value'})
#     False
#     """
#     if isinstance(y, dict):
#         return False
#     return x * y


# def number_compare(a: int, b: int) -> int | float:
#     """
#     >>> number_compare(2, 1)
#     True
#
#     >>> number_compare(1, 2)
#     False
#     """
#
#     if a > b:
#         return True
#     elif a < b:
#         return False






# python -m doctest -v main.py





# Unit тесты


# import unittest
#
# def func(a, b):
#     return a * b
#
# class TestOne(unittest.TestCase):
#     def test_speed_up(self):
#         self.assertEqual(func(2,4), 8, 'Ti chto')


