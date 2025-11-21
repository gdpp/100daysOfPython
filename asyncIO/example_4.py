import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))  # could be awaited directly
    task2 = asyncio.create_task(fetch_data(2))  # could be awaited directly

    result2 = await asyncio.sleep(2.5)

    print("Task 2 fully completed")
    result1 = await task1
    print("Task 1 fully completed")

    return [result1, result2]

t1 = time.perf_counter()

results = main()
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")
