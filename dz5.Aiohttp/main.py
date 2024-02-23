import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

url = 'http://quotes.toscrape.com/'


async def web_async_parce(page: int) -> None:
    all_info = []
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/page/{page}/') as response:
            web_content = await response.text()
            bs_content = BeautifulSoup(web_content, 'html.parser')
            finder = bs_content.findAll('div', {'class': 'price_color'})
            for quote in finder:
                all_info.append(quote.text)
    print(f'Все {len(all_info)} цитат скачаны, на странице {page}')
    print(all_info)



async def main_async():
    start_time = time.time()
    my_list = []

    for i in range(1, 51):
        task = asyncio.create_task(web_async_parce(i))
        my_list.append(task)

    await asyncio.gather(*my_list)

    end_time = time.time() - start_time
    print(f'Асинхронный код спарсил все страницы за {end_time:.2f}')


asyncio.run(main_async())
