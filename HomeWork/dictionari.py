list ={"city": "Москва", "temperature": "20"}
print(list['city'])
print('\n')
list['temperature'] = int(list['temperature'])-5
print(list)
print(list.get('country', 'Россия'))

list['date'] = '27.05.2019'
print(len(list))