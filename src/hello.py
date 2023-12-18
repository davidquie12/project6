
import asyncio
import time

async def async_hello():
    await asyncio.sleep(3)
    print("hello world")
    
async def main():
    res = await asyncio.gather(async_hello())
    return res

if __name__ == '__main__':
    s = time.perf_counter()
    print(asyncio.run(main()))
    elapsed = time.perf_counter()
    print(elapsed -s,"s")