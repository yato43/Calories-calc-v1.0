test = open('test.txt', 'a', encoding='utf-8')
test_str = []
# antropometric data

# height = int(input('Введите рост в см: '))
# weight = int(input('Введите ваш вес в кг: '))
# age = int(input('Введите возраст: '))
height = 189
weight = 142
age = 45

# calculating kkal deficit and PFC
kkal_normal = (((9.99 * weight) + (6.25 * height) - (4.92 * age) - 161) * 0.8)

proteins = 'Норма белков: ' + str(int((kkal_normal * 0.3) / 4)) + ' г'
fats = 'Норма Жиров: ' + str(int((kkal_normal * 0.3) / 9)) + ' г'
carbohydrates = 'Норма Углеводов: ' + str(int((kkal_normal * 0.4) / 4)) + ' г'
kkal_normal = 'Норма калорий: ' + str(int(kkal_normal)) + ' ккал'

normal_list = [kkal_normal, proteins, carbohydrates, fats]
normal_list = '\n'.join(normal_list)
test.write(normal_list)
print(normal_list)





test.close()