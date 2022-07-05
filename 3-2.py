# Задание 2:
# 1. Спросите у пользователя предложение и поделите его по пробелам.
    # Если пользователь ввёл меньше шести слов спросите снова, Не принимайте предложения если оно короче 6 символов, спрашивайте снова и снова.
# 2. Поделите полученный лист на 2 равные части (Если число элементов листа нечетное, то длина первой части должна быть на один жлемент больше)
# 3. Переставьте эти две части местами и запишите в лист.
print('3 секция 2 задание ')
left_list = []
right_list = []
while True:
    sentence = input('Напишите предложение ')
    list_sentence = sentence.split(' ')
    if len(list_sentence) >= 6:
        for i in range(0, len(list_sentence) // 2):
            left_list.append(list_sentence[i])
        for i in range(len(list_sentence) // 2, len(list_sentence)):
            right_list.append(list_sentence[i])
        break
print(right_list + left_list)