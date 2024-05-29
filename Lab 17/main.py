def bin_packing_ffd(items, bin_capacity):
    """
    Функция для решения задачи упаковки в ящики с использованием алгоритма First-Fit Decreasing (FFD).
    :param items: список размеров предметов
    :param bin_capacity: вместимость каждого ящика
    :return: список ящиков с распределенными предметами
    """
    # Сортировка предметов по убыванию размера
    items.sort(reverse=True)

    # Инициализация списка ящиков
    bins = []

    # Распределение предметов по ящикам
    for item in items:
        # Поиск первого подходящего ящика
        bin_found = False
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                bin_found = True
                break

        # Если подходящий ящик не найден, создаем новый
        if not bin_found:
            bins.append([item])

    return bins

# Пример использования
items = [4, 8, 1, 4, 2, 1]
bin_capacity = 10

bins = bin_packing_ffd(items, bin_capacity)

print("Распределение предметов по ящикам:")
for i, bin in enumerate(bins):
    print(f"Ящик {i + 1}: {bin}")
