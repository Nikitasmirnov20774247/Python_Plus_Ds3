# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

data = input('Введите данные: ')
if data.isdigit():
    transformer_data = int(data)
    print("Целое положительное число: ", transformer_data)
else:
    try:
        transformer_data = float(data)
        print('Преобразованно в вещественное число: ', transformer_data)
    except ValueError:
        if data.islower():
            transformer_data = data.upper()
            print('Преобразованно в строку в верхний регистр: ', transformer_data)
        else:
            transformer_data = data.lower()
            print('Преобразованно в строку в нижний регистр: ', transformer_data)