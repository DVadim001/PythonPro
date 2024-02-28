import asyncio


async def green() -> None:
    await asyncio.sleep(1)
    print("GREEN")


async def yellow() -> None:
    await asyncio.sleep(2)
    print("YELLOW")


async def red() -> None:
    await asyncio.sleep(3)
    print("RED")


async def trafficlight():
    while True:
        g = asyncio.create_task(green())
        y = asyncio.create_task(yellow())
        r = asyncio.create_task(red())

        await g
        await y
        await r

asyncio.run(trafficlight())


# Второй вариант
# import asyncio
# lights_list: list = ['GREEN', 'YELLOW', 'RED']
#
#
# async def trafficlight(light: list) -> None:
#     for i in light:
#         print(i)
#
#
# async def collect():
#     l = asyncio.create_task(trafficlight(lights_list))
#     await l
#
# asyncio.run(collect())
