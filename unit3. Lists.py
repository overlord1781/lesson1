#Создание списка
print('Создане списка')
phones_list = ['Xiaomi Mi8', 'iPhone Xs', 'Samsung Galaxy S10', 'iPhone Xs']
phones_count = len(phones_list)
print(phones_list)
print(phones_count)
print('\n')

#Добавление эллементов
print('Добавление эллементов')
phones_list.append('Iphone 6')
phones_count = len(phones_list)
print(phones_list)
print(phones_count)
print('\n')

#Подсчет списка элементов
print('Подсчет элементов')
print(phones_list.count('Iphone 6'))
print(phones_list.count('Iphone 12'))
print('\n')

#Обращение по индексу
print('Обращение по индексу')
print(phones_list[0])
print('\n')

#Срезы
print('Срезы')
print(phones_list[1:3])
print(phones_list[-1])
print(phones_list[:2])
print('\n')

#Поиск индекса эллемента и сортировка 
print('Поиск индекса и сортировка')
print(phones_list.index('iPhone Xs'))
phones_list.sort()
print(phones_list)
print('\n')

#Проверка на вхождение 
print('iPhone Xs' in phones_list)
print('IPhone Xs' in phones_list)
print('\n')

#Удаление элементов
del phones_list[3]
print(phones_list)
phones_list.remove('iPhone Xs')
print(phones_list)