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