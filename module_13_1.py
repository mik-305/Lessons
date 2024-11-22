#import time
import asyncio
name = ''
power = 0



async def start_strongman(name, power):
    for i in range(5):                              # Количество шаров
        print(f'Силач {name} поднял шар № {i+1}')

async def  start_tournament(name, power):
    await asyncio.sleep(1/power)
    print(f'Силач {name} закончил соревнования')


async def main(name, power):
    #task = asyncio.create_task(start_strongman(name, power))
    print(f'Силач {name} начал соревнования')
    task_1 = asyncio.create_task(start_strongman(name, power))
    task_2 = asyncio.create_task(start_tournament(name, power))
    await task_1
    await task_2


asyncio.run(main('Паша', 3 ))
asyncio.run(main('Денис', 4 ))
asyncio.run(main('Apollon', 5 ))
#result = main()