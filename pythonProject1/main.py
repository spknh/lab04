def count_elements(*lists):
    if not lists:
        return 0

    # Преобразуем первый список в множество
    common_elements = set(lists[0])

    # Пересекаем с множествами остальных списков
    for i in lists[1:]:
        common_elements.intersection_update(i)

    return len(common_elements)
