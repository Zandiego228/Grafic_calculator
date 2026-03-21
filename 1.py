my_list = [10, 20, 30, 20, 40, 20, 50]
target = 20

# Сколько раз встречается элемент
count = my_list.count(target)
print(f"Элемент {target} встречается {count} раз(а)")
# Результат: Элемент 20 встречается 3 раз(а)
indices = [i for i, x in enumerate(my_list) if x == target]
print(f"Индексы элемента {target}: {indices}")
# Результат: Индексы элемента 20: [1, 3, 5]