# from threading import Thread
# import requests
# from bs4 import BeautifulSoup
# import time
# from main import url
#
# def web_sync_parce(page: int) -> None:
#     all_quotes = []
#     web = requests.get(f'{url}/page/{page}/')
#     content = web.text
#     bs_content = BeautifulSoup(content, 'html.parser')
#     finder = bs_content.findAll('span', {'itemprop': 'text'})
#     for quote in finder:
#         all_quotes.append(quote.text)
#     print(f'Все {len(all_quotes)} цитат скачаны, на странице {page}')
#     print(all_quotes)
#
#
#
# def main_sync():
#     start_time = time.time()
#     for i in range(1, 11):
#         t1 = Thread(target=web_sync_parce, args=(i,))
#         t1.start()
#     end_time = time.time() - start_time
#     print(f'Многопоточный код спарсил все страницы зв {end_time:.2f}')
#
#
#
# main_sync()