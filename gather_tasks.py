import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    # return some data as a result
    return {"id":id,"data":f"Sample data from coroutine {id}"}

async def main():
    # run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1,2),fetch_data(2,1),fetch_data(3,3))

    # Process the results
    for result in results:
        print(f"Received result: {result}")

# Run the main coroutine
print("The main coroutine is being processed")
asyncio.run(main())


# gather isn't good at error handling 