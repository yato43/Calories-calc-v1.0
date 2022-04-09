file_name = input('Введите название файла: ') + '.txt'
test = open(file_name, 'a', encoding='utf-8')
test_str = []


def diet(kkal, p, f, c):
    while True:
        print('Осталось: \n', 'калорий:', kkal, 'Белков:', p, 'Жиров:', f, 'Углеводов:', c)
        answer = input('Добавить еще продукт? ')
        if answer.lower() == 'да':
            product = input('Введите продукт: ')
            product_weight = int(input('Введите массу продукта: '))
            product_kkal = float(input('Введите кол-во калорий на 100 г.: '))
            product_proteins = float(input('Введите кол-во белков на 100 г.: '))
            product_fats = float(input('Введите кол-во жиров на 100 г.: '))
            product_carbons = float(input('Введите кол-во углеводов на 100 г.: '))
            kkal -= int(product_kkal / 100 * product_weight)
            p -= int(product_proteins / 100 * product_weight)
            f -= int(product_fats / 100 * product_weight)
            c -= int(product_carbons / 100 * product_weight)
            new_record = '\n' + product + ' - ' + str(product_weight) + 'г.'
            test.write(new_record)
        else:
            break
    total = int(kkal), int(p), int(f), int(c)
    return total


# antropometric data

height = int(input('Введите рост в см: '))
weight = int(input('Введите ваш вес в кг: '))
age = int(input('Введите возраст: '))
# height = 189
# weight = 142
# age = 45

# calculating kkal deficit and PFC
kkal_normal = (((9.99 * weight) + (6.25 * height) - (4.92 * age) - 161) * 0.8)

proteins = int((kkal_normal * 0.3) / 4)
fats = int((kkal_normal * 0.3) / 9)
carbohydrates = int((kkal_normal * 0.4) / 4)
kkal_normal = int(kkal_normal)

proteins_str = 'Норма белков: ' + str(proteins) + ' г'
fats_str = 'Норма Жиров: ' + str(fats) + ' г'
carbohydrates_str = 'Норма Углеводов: ' + str(carbohydrates) + ' г'
kkal_normal_str = 'Норма калорий: ' + str(kkal_normal) + ' ккал'

normal_list = [kkal_normal_str, proteins_str, carbohydrates_str, fats_str]
normal_list = '\n'.join(normal_list)
test.write(normal_list)

test.write('\n\nЗавтрак.\n')
print('\n\nЗавтрак. \n')
total = diet(kkal_normal * 0.25, proteins * 0.25, fats * 0.25, carbohydrates * 0.25)
(total_kkal, total_proteins, total_fats, total_carbons) = total

test.write('\n\nланч\n')
print('\n\nланч\n')
total = diet(kkal_normal * 0.15 + total_kkal, proteins * 0.15 + total_proteins, fats * 0.15 + total_fats,
     carbohydrates * 0.15 + total_carbons)
(total_kkal, total_proteins, total_fats, total_carbons) = total

test.write('\n\nОбед.\n')
print('\n\nОбед.\n')
total = diet(kkal_normal * 0.3 + total_kkal, proteins * 0.3 + total_proteins, fats * 0.3 + total_fats,
     carbohydrates * 0.3 + total_carbons)
(total_kkal, total_proteins, total_fats, total_carbons) = total

test.write('\n\nПолдник.\n')
print('\n\nПолдник.\n')
total = diet(kkal_normal * 0.15 + total_kkal, proteins * 0.15 + total_proteins, fats * 0.15 + total_fats,
     carbohydrates * 0.15 + total_carbons)
(total_kkal, total_proteins, total_fats, total_carbons) = total

test.write('\n\nУжин.\n')
print('\n\nУжин.\n')
diet(kkal_normal * 0.15 + total_kkal, proteins * 0.15 + total_proteins, fats * 0.15 + total_fats,
     carbohydrates * 0.15 + total_carbons)

test.close()
