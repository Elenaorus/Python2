#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

dict_list = {'спички': 1, 'посуда': 4, 'запасная одежда': 5, 'палатка': 10, 'запасная обувь': 3}
def backpack(capacity, dict_list):
    packaging_option = []
    for key, value in dict_list.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(backpack(15, dict_list))