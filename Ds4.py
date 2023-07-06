orig_dict = {'спичечный коробок': 0.004, 'фонарик': 1, 'крем от клещей': 0.050, 'бинты': 0.035, 'палатка': 5,
             'нож': 0.200, 'еда': 1.700, 'вода': 1, 'набор посуды': 2, 'компас': 0.40, 'туалетная бумага': 0.400}
res_list = []

print(f'\nОригинальный словарь: {orig_dict}\n')
orig_dict = dict(sorted(orig_dict.items(), key=lambda item: item[1]))
weight = int(input('Введите грузоподъемность рюкзака в кг: '))

for item in orig_dict:
    if orig_dict[item] < weight:
        weight = weight - orig_dict[item]
        res_list.append(item)

print(f'\nСписок допустимых вещей для рюкзака: {res_list}')