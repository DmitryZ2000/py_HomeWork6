# 9 Уровней применения функции zip в Python

matrix = [[1, 2, 3], [1, 2, 3]]
print(matrix)
# Как транспонировать эту матрицу?
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)
print(*matrix_T)


print('\n', 'Level 0', '\n')

id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
record = zip(id, leaders)
print(record) # <zip object at 0x7f266a707d80>
print(list(record)) # [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]

print('\n','Level 1 Zip работает с любым количеством итерируемых объектов', '\n')

id = [1, 2, 3, 4]
record = zip(id)
print(list(record)) # [(1,), (2,), (3,), (4,)]

id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
sex = ['male', 'male', 'male', 'male']
record = zip(id, leaders, sex)
print(list(record)) # [(1, 'Elon Mask', 'male'), (2, 'Tim Cook', 'male'), (3, 'Bill Gates', 'male'), (4, 'Yang Zhou', 'male')]

print('\n', 'Level 2: работа с неравными по длине аргументами', '\n')

id = [1, 2]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
record = zip(id, leaders)
print(list(record)) # [(1, 'Elon Mask'), (2, 'Tim Cook')]

from itertools import zip_longest

id = [1, 2]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
long_record = zip_longest(id, leaders)
print(list(long_record)) # [(1, 'Elon Mask'), (2, 'Tim Cook'), (None, 'Bill Gates'), (None, 'Yang Zhou')]

long_record_2 = zip_longest(id, leaders, fillvalue='Top') #Заполнение пустым значением по умолчанию
print(list(long_record_2)) # [(1, 'Elon Mask'), (2, 'Tim Cook'), ('Top', 'Bill Gates'), ('Top', 'Yang Zhou')]

print('\n', 'Level 3: операция распаковывания', '\n')
record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
print(record)
id, leaders = zip(*record) #Распоковка * и zip
print(id) # (1, 2, 3, 4)
print(leaders) # ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')

print(' или ')
record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
print(*record)  # распаковываем список одной звёздочкой
# (1, 'Elon Mask') (2, 'Tim Cook') (3, 'Bill Gates') (4, 'Yang Zhou')

id, leaders = zip((1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou'))
print(id) # (1, 2, 3, 4)
print(leaders) # ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')

print('\n', 'Level 4: Создание и обновление словарей','\n')

id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']

# создаём словарь, используя «dict comprehension»
leader_dict = {i: name for i, name in zip(id, leaders)}
print(leader_dict) # {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# создаём словарь, используя функцию «dict»
leader_dict_2 = dict(zip(id, leaders))
print(leader_dict_2) # {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# обновляем
other_id = [5, 6]
other_leaders = ['Larry Page', 'Sergey Brin']
leader_dict.update(zip(other_id, other_leaders))
print(leader_dict) # {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou', 5: 'Larry Page', 6: 'Sergey Brin'}

print('\n', 'Level 5: функция zip вместо циклов for', '\n')

numbers = [12, 3, 7, 15, 8]
diff = [a-b for a, b in zip(numbers, numbers[1:])]
print(numbers)
print(numbers[1:])
print(diff)

print('\n', 'Level 6: сортировка списков', '\n')

list1 = [3, 2, 4, 1, 1]
list2 = ['three', 'two', 'four', 'one', 'one2']
print(list(zip(list1, list2)))
print(sorted(zip(list1, list2)))
print(*sorted(zip(list1, list2)))

list1, list2 = zip(*sorted(zip(list1, list2)))

print(list1)
print(list2)

print('\n', 'Level 7: применение функции zip в циклах for', '\n')

products = ["cherry", "strawberry", "banana"]
price = [2.5, 3, 5]
cost = [1, 1.5, 2]
for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is £{p-c}!')

print('\n', 'Level 8: транспонирование матрицы', '\n')

matrix = [[1, 2, 3], [1, 2, 3]]
print(*matrix)
print(list(zip(*matrix)))

matrix_T = [list(i) for i in zip(*matrix)]

print(matrix_T) # [[1, 1], [2, 2], [3, 3]]