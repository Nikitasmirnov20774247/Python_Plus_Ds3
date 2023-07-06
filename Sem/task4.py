# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

old_list = [1, 2, 2, 2, 4, 7, 3, 7, 8, 9]
new_dict = {}
new_list = []

for i in old_list:
    if i not in new_dict.keys():
        new_dict[i] = [i]
    else:
        new_dict[i].append(i)

for item in old_list:
    if len(new_dict[item]) != 2:
        new_list.append(item)

print(new_list)