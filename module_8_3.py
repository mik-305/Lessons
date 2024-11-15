class IncorrectVinNumber(Exception):
    message = 'Некорректный тип данных для номеров'

class IncorrectCarNumbers(Exception):
    message = 'Неверная длина номера'

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        vin_namber = __vin
        print('-2-vin_namber = ', vin_namber)
        print(type(vin_namber))

    def __is_valid_vin(vin_number):
        if not isinstance(vin_namber, int):                 # если VIN не целое число
            print('VIN не целое число!')
            raise IncorrectVinNumber('!!!!!!!!!!!!!!!!')
        #        raise Exception('VIN - не целое число')

        #print(a)
        self.__numbers = __numbers
        print('-3->', model,__vin,  __numbers)
        def __is_valid_numbers(numbers):
            if numbers.isinstance != str:                   # если НОМЕР не строка
                raise Exception('НОМЕР - не строка симолов')

#----------------------------------------------------


try:
  first = Car('Model1', 100000010.1, 'f123dj')
except IncorrectVinNumber as exc:
  #print(exc.message)
  print('777777777777')
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')
