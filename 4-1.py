'''
4 секция <------------------------------------------------------------------------------->
'''
# Задание 1:
    # Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
    # 1. У пользователя просят выбрать знак
    # 2. Просят ввести 1-ое число
    # 3. Просят ввести 2-ое число
    # 4. Вывести результат
    # 5. После результата спросить у пользователя хочет он закончить или нет,
    # если нет то калькулятор должен запускатся сначала
    # 6. Учесть то что деление на ноль невозможно
print('4 секция задание 1')
while True:
    leave = input('Вы хотите выйти ? (д/н) ')
    if leave == 'д':
        break
    act = input('Введите знак операции (+, -, *, /) ')
    a = int(input('Введите 1-ое число '))
    b = int(input('Введите 2-ое число '))
    answer = 0
    if act == '/' and b == 0:
        print('Деление на ноль невозможно ')
        break
    if act == '+':
        answer = a + b
    elif act == '-':
        answer = a - b
    elif act == '*':
        answer = a * b
    elif act == '/':
        answer = a / b
    print(f'{a} {act} {b} = {answer}')