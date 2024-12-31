import time
import asyncio

async def do_work(s:str, delay_s:float=1.0):
    print(f"{s} started")
    await asyncio.sleep(delay_s)
    print(f"{s} done")

async def main():
    start = time.perf_counter()

    todo = ['get package','laundry','bake cake']

    tasks = []
    for item in todo:
        tasks.append(asyncio.create_task(do_work(item)))
    _,_,_ = await tasks[0], await tasks[1], await tasks[2]
    end = time.perf_counter()
    print(f"It took: {end-start:.2f}s")

asyncio.run(main())