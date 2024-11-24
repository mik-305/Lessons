import asyncio
async def start_strongman(name, power):
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял шар № {i+1}.')
    print(f'Силач {name} закончил соревнования')
async def start_tournament(name, power):
   # print(f'Силач {name} начал соревнования.')


    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    #task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    #await task3

#async def main(name, power):
#    task1 = asyncio.create_task(start_strongman(name, power))
#    await task1


print('Силач Pasha начал соревнования.')
print('Силач Denis начал соревнования.')
print('Силач Apollon начал соревнования.')
asyncio.run(start_tournament('Pasha', 3))
asyncio.run(start_tournament('Denis', 4))
asyncio.run(start_tournament('Apollon', 5))
