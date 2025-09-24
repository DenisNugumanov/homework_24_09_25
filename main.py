######### 1 Задача ########

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recipe_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            product, quantity, word = recipe
            ingredients.append({'product': product, 'quantity': int(quantity), 'measure': word})
        file.readline()
        cook_book[recipe_name] = ingredients

print('\nКУЛИНАРНАЯ КНИГА, СЛОВАРЬ К ЗАДАНИЮ 1')
print('{')
for recipe_name, ingredients in cook_book.items():
    print(f"  '{recipe_name}': [")
    for i, ingredient in enumerate(ingredients):
        if i == len(ingredients) - 1:  # последний элемент
            print(
                f"    {{'product': '{ingredient['product']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}}")
        else:
            print(
                f"    {{'product': '{ingredient['product']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}},")
    if recipe_name == list(cook_book.keys())[-1]:  # последний рецепт
        print("  ]")
    else:
        print("  ],")
print('}')


########## 2 Задача #########

def get_shop_list_by_dishes(person_count, dishes):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                product_name = consist['product']
                quantity_needed = consist['quantity'] * person_count

                if product_name in result:
                    result[product_name]['quantity'] += quantity_needed
                else:
                    result[product_name] = {
                        'measure': consist['measure'],
                        'quantity': quantity_needed
                    }
        else:
            print(f'Блюда "{dish}" нет в кулинарной книге')

    print('{')
    for i, (product, info) in enumerate(result.items()):
        if i == len(result) - 1:  # Последний элемент без запятой
            print(f"  '{product}': {{'measure': '{info['measure']}', 'quantity': {info['quantity']}}}")
        else:
            print(f"  '{product}': {{'measure': '{info['measure']}', 'quantity': {info['quantity']}}},")
    print('}')
    return result


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