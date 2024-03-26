str = input('camelCase: ')

lst = list(str)

new_lst = []

for i in range(len(lst)):
    if lst[i].islower() == True:
        lst[i] = lst[i]
    else:
        lst.insert(i,'_')
        i = i + 1
        lst[i] = lst[i].lower()

snake_case = ''.join(lst)
print('snake_case: ', snake_case)