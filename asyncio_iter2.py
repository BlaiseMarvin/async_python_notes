import asyncio
from random import randint
import time

MAX = 898
async def generate_random_numbers(total):
    for _ in range(total):
        await asyncio.sleep(2)
        yield randint(1,MAX)

async 
async def main():
    start = time.perf_counter()
    # numbers = [num async for num in generate_random_numbers(10)]
    # numbers2 = [num async for num in generate_random_numbers(10)]
    await asyncio.gather(await generate_random_numbers(10), await generate_random_numbers(10))
    # numbers = [num for num in results[0]]
    # numbers2 = [num for num in results[1]]
    # print(numbers, numbers2)
    end = time.perf_counter()
    print(f"Task Duration: {round(end-start, 2)}")

asyncio.run(main())
