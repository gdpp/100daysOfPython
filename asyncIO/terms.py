import asyncio
import time


def sync_function(test_param: str) -> str:
    print("This is a syncronous function")

    time.sleep(0.1)

    return f"Sync result: {test_param}"

# Also known as a COROUTINE function


async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function.")
    await asyncio.sleep(0.1)

    return f"Async result: {test_param}"


async def main():
    # sync_result = sync_function("Test")
    # print(sync_result)
    # loop = asyncio.get_running_loop()
    # future = loop.create_future()  # A promise-like object
    # print(f'Empty future: {future}')

    # future.set_result("Future Result: Test")
    # future_result = await future
    # print(future_result)

    # coroutine_object = async_function("Test")
    # print(coroutine_object)

    # coroutine_result = await coroutine_object
    # print(coroutine_result)

    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)


if __name__ == '__main__':
    asyncio.run(main())
