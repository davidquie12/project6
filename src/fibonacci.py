import asyncio
import sys
import random as rand

def fibonacci(num : int):
    num1, num2= 0,1
    for i in range(num):
        yield num1
        num1, num2 = num2, num1 + num2
         
async def main(count : int, num : int):
    res = await asyncio.gather(async_fibanocci(10))
    return res

# Using the generator
fib_gen = fibonacci(10)
print(list(fib_gen)) 

'''if __name__ == "__main__":
    asyncio.run(main(0,10))
'''

async def taak1(count : int, r : int):
    print("taak1 :",r,"s")
    await asyncio.sleep(r)


async def taak2(count : int, r : int):
    print("taak2",r,"s")
    await asyncio.sleep(r)

async def taak3(count : int, r : int):
    print("taak3",r,"s")
    await asyncio.sleep(r)

async def async_fibanocci(num : int):
    num1, num2= 0,1
    for i in range(num):
        yield num1
        num1, num2 = num2, num1 + num2
        print(num2)
        
        await asyncio.sleep(5)
        
        
async def async_chain(count : int, num : int, r : list):
    await taak1(count,r[0])
    await taak2(count,r[1])
    await taak3(count,r[2])
    async for fib_num in async_fibanocci(num):
        pass

        
async def main(*args):
    await asyncio.gather(*(async_chain(count,num,r) for count , num , r in args))    
    
    
    
if __name__ == "__main__":
    while True:
        r1 = rand.randint(1,5)
        r2 = rand.randint(1,5) 
        r3 = rand.randint(1,5) 
        
        rands = [r1,r2,r3]
        args = [0,10,rands] 
        result=asyncio.run(main(args))
        print(result)