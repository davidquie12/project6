import asyncio
import time
import random
async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")
    
async def main():
    await asyncio.gather(count(), count(), count())
    
# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)
async def makeRandom(idx : int, threshold : int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0,10)
    
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0,10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    result = await asyncio.gather(*( makeRandom(i,10 -i -1 ) for i in range(3)))
    return result

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

    
    
     
     
    
"""if  __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    
"""
    
    