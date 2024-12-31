import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay,id):
    print("Fetching data....id",id)
    await asyncio.sleep(delay) # simulate an i/o operation with a sleep
    print("Data fetched, id:", id)
    return {"data":"Some data", "id":id} # return some data

# define another corountine that calls the first coroutine
async def main():
    task1 = fetch_data(2,1)
    task2 = fetch_data(2,2)

    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")


# run the main coroutine
asyncio.run(main())