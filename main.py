######### 1 Задача ########

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            product, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'product': product,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()  # пропускаем пустую строку
        cook_book[recipe_name] = ingredients

print('\nКУЛИНАРНАЯ КНИГА, СЛОВАРЬ К ЗАДАНИЮ 1')
print('{')
for recipe_name, ingredients in cook_book.items():
    print(f"  '{recipe_name}': [")
    for ingredient in ingredients:
        print(
            f"    {{'product': '{ingredient['product']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}}",
            end='')
        if ingredient != ingredients[-1]:  # добавляем запятую если не последний элемент
            print(',')
        else:
            print()
    print("  ]" + ("," if recipe_name != list(cook_book.keys())[-1] else ""))
print('}')


########## 2 Задача #########

def get_shop_list_by_dishes(person_count, dishes):
    shopping_list = {}

    for dish_name in dishes:
        if dish_name not in cook_book:
            print(f'Блюда "{dish_name}" нет в кулинарной книге')
            continue

        for ingredient in cook_book[dish_name]:
            product_name = ingredient['product']
            quantity_needed = ingredient['quantity'] * person_count

            if product_name in shopping_list:
                shopping_list[product_name]['quantity'] += quantity_needed
            else:
                shopping_list[product_name] = {
                    'measure': ingredient['measure'],
                    'quantity': quantity_needed
                }

    # Красивый вывод без итерирования по индексам
    print('{')
    products = list(shopping_list.items())
    for product, details in products:
        is_last_product = (product == products[-1][0])
        comma = "" if is_last_product else ","
        print(f"  '{product}': {{'measure': '{details['measure']}', 'quantity': {details['quantity']}}} {comma}")
    print('}')

    return shopping_list


print('\nДВА БЛЮДА НА ДВЕ ПЕРСОНЫ, ЗАДАНИЕ 2')
get_shop_list_by_dishes(2, ['Салат Греческий', 'Курица с картофелем'])


########## 3 Задача #########

name_dict = {}

with open('1.txt', encoding='utf-8') as f1:
    name_1 = '1.txt'
    count_1 = len(f1.readlines())
    with open('2.txt', encoding='utf-8') as f2:
        name_2 = '2.txt'
        count_2 = len(f2.readlines())
        with open('3.txt', encoding='utf-8') as f3:
            name_3 = '3.txt'
            count_3 = len(f3.readlines())
            name_dict = {count_1: [name_1, count_1], count_2: [name_2, count_2], count_3: [name_3, count_3]}

sorted_dict = dict(sorted(name_dict.items()))
with open('result.txt', 'a', encoding='utf-8') as file:
    for value in sorted_dict.values():
        for i in value:
            file.write(f'{i}\n')
with open('result.txt', encoding='utf-8') as result_file:
    print(result_file.read())