def test (T):
    result = {}
    for item in T:
        result[item[0]] = item[1:]
    return result

L = ['poonam','ganesh','aruna','abhiraj']

#to convert list into dictionary.
print('converted into tuple:')
print(test(L))