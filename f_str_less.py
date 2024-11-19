team1_num = 5           # Использование %
team2_num = 6
print('В команде Мастера кода участников: %s!' % (team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('')

score_1 = 40            # Использование format
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
print('')

score_1 = 40            # Использование f-строки
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')