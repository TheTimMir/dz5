def input_int(message=''):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Некорректное значение!')
        except Exception as error:
            print(f'Непредвиденная ошибка: {error}')
        else:
            return result


a = input_int('Введите a:')
b = input_int('Введите b:')

print(f'{a} + {b} = {a + b}')
