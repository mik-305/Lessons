import asyncio

async def start_strongman(name: str, power: int):  # Асинхронная функция для имитации соревнований
    print(f'Силач {name} начал соревнования.')
    print('')
    for i in range(1, 6):  # Каждый силач поднимает 5 шаров
        await asyncio.sleep(1 / power)          # Задержка зависит от силы
        print(f'Силач {name} поднял шар № {i}')
    print(f'Силач {name} закончил соревнования.')
    
async def start_tournament():                   # Асинхронная функция для проведения соревнований

    atlets = [                          # Список наших участников соревнований
        ('Паша', 3),
        ('Денис', 4),
        ('Аполлон', 5)
    ]


    tasks = [asyncio.create_task(start_strongman(name, power)) for name, power in atlets] # Каждый атлет выступает


    await asyncio.gather(*tasks)        # Ожидание завершения выступления всех атлетов



asyncio.run(start_tournament())         # Начинаем соревнование
