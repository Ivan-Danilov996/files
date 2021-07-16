import os

cook_book = {}

with open('text.txt', 'r', encoding="utf-8") as file:
    for line in file:
        if line.strip() == '':
            pass
        else:
            name = line.strip()
            cook_book[name] = []
            count = file.readline().strip()
            for i in range(int(count)):
                list_items = file.readline().strip().split('|')
                cook_book[name].append({
                    'ingredient_name': list_items[0],
                    'quantity': list_items[1],
                    'measure': list_items[2]
                })

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredients = {
                'measure': ingredient['measure'],
                'quantity': int(ingredient['quantity']) * person_count
            }
            shop_list[ingredient['ingredient_name']] = ingredients
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

files_path = os.path.join(os.getcwd(), 'files/')
files = os.listdir(files_path)

data = {}

for file_name in files:
    if file_name != 'new-file.txt':
        with open(files_path + file_name, 'r', encoding="utf-8") as file:
            line_count = 0
            for line in file:
                line_count += 1
            data[file_name] = line_count

sorted_files = sorted(data.items(), key=lambda count: count[1])

with open(files_path + 'new-file.txt', 'w+', encoding="utf-8") as new_file:
    new_file.write('')

for file_name in sorted_files:
    with open(files_path + file_name[0], 'r', encoding="utf-8") as file:
        text = file.read()
        with open(files_path + 'new-file.txt', 'a', encoding="utf-8") as new_file:
            new_file.write(file_name[0] + '\n' + str(file_name[1]) + '\n' + text + '\n')
