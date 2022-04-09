test = open('test.txt', 'a', encoding='utf-8')
test_str = []

def diet (kkal, p, f, c):
    while True:
        print('Осталось: \n','калорий:',kkal,'Белков:', p,'Жиров:', f,'Углеводов:', c)
        answer = input('Добваить еще продукт? ')
        if answer.lower() == 'да':
            product = input('Введите продукт: ')
            product_weight = int(input('Введите массу продукта: '))
            product_kkal = float(input('Введите кол-во калорий на 100 г.: '))
            product_proteins = float(input('Введите кол-во белков на 100 г.: '))
            product_fats = float(input('Введите кол-во жиров на 100 г.: '))
            product_carbons = float(input('Введите кол-во углеводов на 100 г.: '))
            kkal -= int(product_kkal/100 * product_weight)
            p -= int(product_proteins/100 * product_weight)
            f -= int(product_fats/100 * product_weight)
            c -= int(product_carbons/100 * product_weight)
            new_record ='\n' + product + ' - ' + str(product_weight) + 'г.'
            test.write(new_record)
        else:
            break
# antropometric data

# height = int(input('Введите рост в см: '))
# weight = int(input('Введите ваш вес в кг: '))
# age = int(input('Введите возраст: '))
height = 189
weight = 142
age = 45

# calculating kkal deficit and PFC
kkal_normal = (((9.99 * weight) + (6.25 * height) - (4.92 * age) - 161) * 0.8)

proteins = int((kkal_normal * 0.3) / 4)
fats = int((kkal_normal * 0.3) / 9)
carbohydrates = int((kkal_normal * 0.4) / 4)
kkal_normal = int(kkal_normal)

proteins_str = 'Норма белков: ' + str(kkal_normal) + ' г'
fats_str = 'Норма Жиров: ' + str(kkal_normal) + ' г'
carbohydrates_str = 'Норма Углеводов: ' + str(kkal_normal) + ' г'
kkal_normal_str = 'Норма калорий: ' + str(kkal_normal) + ' ккал'


normal_list = [kkal_normal_str, proteins_str, carbohydrates_str, fats_str]
normal_list = '\n'.join(normal_list)
test.write(normal_list)

test.write('\n\nЗавтрак.')

test.write('\n\nланч')

test.write('\n\nОбед.')

test.write('\n\nПолдник')

test.write('\n\nУжин')



diet(int(kkal_normal), int(proteins), int(fats), int(carbohydrates))

test.close()
