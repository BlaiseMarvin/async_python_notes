import time
import asyncio

async def do_work(s:str, delay_s:float=1.0):
    print(f"{s} started")
    await asyncio.to_thread(time.sleep(delay_s))
    print(f"{s} done")

async def main():
    start = time.perf_counter()

    todo = ['get package','laundry','bake cake']

    tasks = [do_work(item) for item in todo]

    await asyncio.gather(*tasks)
    
    end = time.perf_counter()
    print(f"It took: {end-start:.2f}s")

asyncio.run(main())