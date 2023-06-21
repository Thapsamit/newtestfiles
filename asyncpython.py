import asyncio


async def rt():
    loop = asyncio.get_running_loop()
    print("from main", loop)


loop = asyncio.get_event_loop()
loop.run_until_complete(rt())
