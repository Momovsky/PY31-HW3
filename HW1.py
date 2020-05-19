def recipe_rewrite(output_name):
    with open (output_name, 'r', encoding='utf-8') as recipes:
        cook_book = {}
        def recipe_rewrite():
            dish = recipes.readline().strip()
            if dish:
                cook_book[dish] = []
                ingredient_number = recipes.readline()
                for line in range(int(ingredient_number)):
                    ingredient = recipes.readline().strip().split(' | ')
                    ingredient_dictionary = {'ingredient name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                    cook_book[dish].append(ingredient_dictionary)
            else:
                return(cook_book)
            recipes.readline()
            recipe_rewrite()
        recipe_rewrite()
    return(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipe_rewrite('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient name'] not in shop_list:
                    shop_list[ingredient['ingredient name']] = {'measure': ingredient['measure'], 'quantity': (int(ingredient['quantity'])*person_count)}
                else:
                    shop_list[ingredient['ingredient name']]['quantity'] += (int(ingredient['quantity'])*person_count)
    return(shop_list)

print(recipe_rewrite('recipes.txt'))
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10))
