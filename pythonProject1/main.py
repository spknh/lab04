def count_elements(*lists):
    if not lists:
        return 0

    # Преобразуем первый список в множество
    common_elements = set(lists[0])

    # Пересекаем с множествами остальных списков
    for i in lists[1:]:
        common_elements.intersection_update(i)

    return len(common_elements)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 1]
list3 = [4, 1, 6, 7]

result = count_elements(list1, list2, list3)
print(f"Количество одинаковых элементов: {result}")