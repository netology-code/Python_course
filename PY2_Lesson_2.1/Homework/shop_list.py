#Можно ли собрать библиотеку из рецептов по разделам:
# закуски, 2-е, десерты. 
# Потом создать функцию которая будет выводить список и количество продуктов  при 
# выборе 1,2,3 блюда на _____ персон.  В итоге вывести на печать список покупок.

cook_book = {
    'Омлет': {
        'name': 'Омлет',
        'type': '2-е',
        'ingridients': [
                {'product' : 'Яйца', 'quantity': 2, 'unit': 'шт'},
                {'product' : 'Молоко', 'quantity': 50, 'unit': 'мл'},
                {'product' : 'Помидор', 'quantity': 100, 'unit': 'г'},
        ]
    }, 
    'Яблочный пирог': { 
        'name': 'Яблочный пирог',
        'type': 'Десерт',
        'ingridients': [
                {'product' : 'Яйца', 'quantity': 1, 'unit': 'шт'},
                {'product' : 'Мука', 'quantity': 300, 'unit': 'г'},
                {'product' : 'Масло', 'quantity': 60, 'unit': 'г'},
                {'product' : 'Яблоки', 'quantity': 80, 'unit': 'г'},
        ]
    },
    'Суп': {
        'name': 'Суп',
        'type': '1-е',
        'ingridients': [
                {'product' : 'Вода', 'quantity': 100, 'unit': 'мл'},
                {'product' : 'Помидор', 'quantity': 300, 'unit': 'г'},
        ]
    }, 
}

def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dish['ingridients']:
            new_shop_item = dict(ingridient)
            # пересчитали ингрединты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))

def create_shop_list(people_count, first_dish, second_dish, third_dish):
    # получить блюда из кулинарной книги
    dish1 = cook_book[first_dish]
    dish2 = cook_book[second_dish]
    dish3 = cook_book[third_dish]
    dishes = [dish1, dish2, dish3]
    #заполнили список покупок
    shop_list = get_shop_list_by_dishes(dishes, people_count)
    # Вывести список покупок
    print_shop_list(shop_list)

print('Выберите первое блюдо: ')
first_dish = input()
print('Выберите второе блюдо: ')
second_dish = input()
print('Выберите третье блюдо: ')
third_dish = input()
print('На сколько человек?')
people_count = int(input())

print('Список покупок: ')
create_shop_list(people_count, first_dish, second_dish, third_dish)