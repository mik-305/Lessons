class Car:
    def __init__(self, model, __vin, __numbers):
        global vin_number, numbers
        self.model = model
        vin_number = __vin
        numbers = __numbers
        def __is_valid_vin(vin_number):          # Начало процедуры проверки корректности VIN
            if not isinstance(vin_number, int):  # если VIN не целое число
                raise IncorrectVinNumber('Некорректный VIN-номер!')
            if vin_number < 1000000 or vin_number > 9999999: # Если VIN вне корректного диапазона
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            return
        __is_valid_vin(vin_number)
        def __is_valid_numbers(numbers):        # Начало процедуры проверки госномера
            if not isinstance(numbers, str):  # если госномер  не строка
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if len(numbers)!=6:                 # проверка длины госномера
                raise IncorrectCarNumbers('Неверная длина номера')
            return

        __is_valid_numbers(numbers)
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message






try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
  