import asyncio


"""
This is a simple illustration of what are coroutines
"""


async def say_hi():
    return 'hi'

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    promise = say_hi()
    print(promise)
    print(loop.run_until_complete(promise))
