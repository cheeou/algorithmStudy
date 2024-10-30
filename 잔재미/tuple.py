tuple_data = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')

print(tuple_data[1:])

print(type(tuple_data))

print(list(tuple_data))

list_data = list(tuple_data)
list_data.append('fun-coding6')
print(list_data)

tuple_data_2 = tuple(list_data)
print(tuple_data_2)

# empty tuple,list,dic

tupleData = tuple()
listData = list()
dicData = dict()

print(type(tupleData), type(listData), type(dicData))

# dict

english_dict = {'environment': '환경', 'company':'회사', 'government':'정부'}

print(english_dict.keys())

