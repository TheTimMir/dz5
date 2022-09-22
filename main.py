class NegativeDamageError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def attack(damage):
    if damage < 0:
        raise NegativeDamageError('Передан отрицательный урон')
    print(f'Нанесено {damage} урона.')


try:
    attack(-1)
except NegativeDamageError:
    print('Передан отрицательный урон!')
except Exception as error:
    print(f'Что-то пошло не так: {error}')

try:
    a = 6
    b = 4

    print(a / b)
except ZeroDivisionError as error:
    print(f'Невозможно посчитать результат: {error}!')
except TypeError as error:
    print(f'Недопустимый тип данных у одного из операндов!')
except Exception as error:
    print(f'Непредвиденная ошибка: {type(error)}: {error}')
else:
    print('Всё ок!')
finally:
    print('Этот блок выполнится в любом случае')

print('Программа завершилась')