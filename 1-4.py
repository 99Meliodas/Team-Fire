# Задание №4:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30" и возвращает dictionary разделённую по значениям даты:

# date = {
# "year": "2020",
# "month": "10",
# .....
# }
print('1 секция задание 4')
date_input = input('Введите дату в формате гггг-мм-дд часы:минуты ')
date_list = date_input.split(' ')
y_m_d = date_list[0].split('-')
hours_minutes = date_list[1].split(':')
date_dict = {
    'Year': y_m_d[0],
    'Month': y_m_d[1],
    'Day': y_m_d[2],
    'Hours': hours_minutes[0],
    'Minutes': hours_minutes[1]
}
print(date_dict)
