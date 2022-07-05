'''
2 секция <------------------------------------------------------->
'''
# Задача 3
# Здесь замешаны разные типы данных.
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
print('2 секция 3 задание ')
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
set_spisok1 = set(spisok_1)
set_spisok_2 = set(spisok_2)

print(set_spisok_2.difference(set_spisok1))
