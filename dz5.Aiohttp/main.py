import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'


# Асинхронный парсинг
async def async_parce(page: int) -> None:
    names = []
    prices = []
    in_stocks = []
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/catalogue/page-{page}.html') as response:
            web = await response.text()
            bs_content = BeautifulSoup(web, 'html.parser')
            finder_name = bs_content.findAll('h3')
            finder_price = bs_content.findAll('p', {'class': 'price_color'})
            finder_ahref = bs_content.find_all('img')
            finder_in_stock = bs_content.findAll('p', {'class': 'instock availability'})

            for name in finder_name:
                names.append(name.text)

            for price in finder_price:
                prices.append(price.text)

            ahrefs = [img['src'] for img in finder_ahref if 'src' in img.attrs]

            for in_stock in finder_in_stock:
                in_stocks.append(in_stock.text)

    print(f'Книги в количестве {len(names)}\n по названиям: {names}\n '
          f'ценам: {prices}\n '
          f'с ссылкой на изображение обложки: {ahrefs}\n '
          f'скачаны, на странице {page}\n')


async def main_async():
    start_time = time.time()
    my_list = []

    for i in range(1, 51):
        task = asyncio.create_task(async_parce(page=i))
        my_list.append(task)

    await asyncio.gather(*my_list)

    end_time = time.time() - start_time
    print(f'Асинхронный код спарсил все страницы за {end_time:.2f}')


asyncio.run(main_async())


# # Синхронный парсинг
# def sync_parce(page: int) -> None:
#     names = []
#     prices = []
#     in_stocks = []
#
#     web = requests.get(f'{url}/catalogue/page-{page}.html')
#     content = web.text
#     bs_content = BeautifulSoup(content, 'html.parser')
#     finder_name = bs_content.findAll('h3')
#     finder_price = bs_content.findAll('p', {'class': 'price_color'})
#     finder_ahref = bs_content.find_all('img')
#     finder_in_stock = bs_content.findAll('p', {'class': 'instock availability'})
#
#     for name in finder_name:
#         names.append(name.text)
#
#     for price in finder_price:
#         prices.append(price.text)
#
#     ahrefs = [img['src'] for img in finder_ahref if 'src' in img.attrs]
#
#     for in_stock in finder_in_stock:
#         in_stocks.append(in_stock.text)
#
#     print(f'Книги в количестве {len(names)}\n по названиям: {names}\n '
#           f'ценам: {prices}\n '
#           f'с ссылкой на изображение обложки: {ahrefs}\n '
#           f'скачаны, на странице {page}\n')
#
#
# def main_sync():
#     start_time = time.time()
#     for i in range(1, 51):
#         sync_parce(page=i)
#     end_time = time.time() - start_time
#     print(f'Синхронный код спарсил все страницы за {end_time:.2f}')
#
#
# main_sync()
