orig_str = '''Кошка (лат. Felis catus) — домашнее животное, одно из наиболее популярных (наряду с собакой) «животных-компаньонов».
    С точки зрения научной систематики, домашняя кошка — млекопитающее семейства кошачьих отряда хищных.
    Одни исследователи рассматривают домашнюю кошку как подвид дикой кошки, другие — как отдельный биологический вид.
    Являясь одиночным охотником на грызунов и других мелких животных, кошка — социальное животное,
    использующее для общения широкий диапазон звуковых сигналов, а также феромоны и движения тела.
    В настоящее время в мире насчитывается около 600 млн домашних кошек, выведено около 200 пород,
    от длинношёрстных (персидская кошка) до лишённых шерсти (сфинксы),
    признанных и зарегистрированных различными фелинологическими организациями.
    На протяжении 10 000 лет кошки ценятся человеком,
    в том числе за способность охотиться на грызунов и других домашних вредителей,
    а также за умение забавлять и утешать детей.'''

orig_str = orig_str.lower()
duplicate_dict = {}
orig_list = []
new_list = []
punc = '''.,!?/\|"'[]{}<>`~@#№$%^&*()-+=_—'''

for elem in orig_str:
    if elem in punc or elem.isdigit():
        orig_str = orig_str.replace(elem, "")

orig_list = orig_str.split(' ')

for item in orig_list:
    if item == '' or len(item) == 1:
        pass
    else:
        if item in new_list:
            if item in duplicate_dict:
                duplicate_dict[item] += 1
            else:
                duplicate_dict[item] = 2
        else:
            new_list.append(item)

duplicate_dict = sorted(duplicate_dict.items(), key=lambda item: item[1], reverse=True)

while len(duplicate_dict) > 10:
    duplicate_dict.pop()

duplicate_dict = dict(duplicate_dict)
print(duplicate_dict)