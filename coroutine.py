import asyncio

# define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching Data.....")
    await asyncio.sleep(delay)
    print("Data Fetched")
    return {"data":"Some data"}


# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(12)
    # Await the fetch_data coroutine, pausing execution of main until fetch data completes
    print("Now awaiting the fetching data coroutine")
    result = await task
    print(f"Received result: {result}")
    print(f"End of main coroutine")

# Run the main coroutine
asyncio.run(main())