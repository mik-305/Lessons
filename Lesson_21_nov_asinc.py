import time
import asyncio

async def notification():
    time.sleep(3)
    print('Дo доставки осталось 10 мин')

async def main():
    task = asyncio.create_task(notification())
    #await notification()
    print('Собраеимся в поездку')
    print('Едим')

asyncio.run(main())
