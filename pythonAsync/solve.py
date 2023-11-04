import asyncio 

async def fun() :
    print("Hello")
    await asyncio.sleep(15);
    print('Hell Lost')

asyncio.run(fun())