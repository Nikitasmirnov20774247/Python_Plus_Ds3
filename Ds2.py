orig_list = [1, 2, 2, 3, 4, 5, 5, 6, 1, 9, 7, 7, 8, 5]
new_list = []
duplicate_list = []

for item in orig_list:
    if item in new_list:
        if item in duplicate_list:
            pass
        else:
            duplicate_list.append(item)
    else:
        new_list.append(item)

print(f'Оригинальный список: {orig_list}')
print(f'Список с дублирующимися элементами: {duplicate_list}')
print(f'Новый список без дублиуатов: {new_list}')