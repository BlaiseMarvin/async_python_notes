import asyncio
import time

async def do_io():
    print("io start")
    await asyncio.sleep(2)
    print("io end")

async def do_other_things():
    print("doing other things")

def main() -> None:
    loop = asyncio.get_event_loop()
    start = time.perf_counter()
    loop.run_until_complete(do_io())
    loop.run_until_complete(do_other_things())
    end = time.perf_counter()
    loop.close()
    print(f"Duration: {round(end-start,2)}")

if __name__ == "__main__":
    main()