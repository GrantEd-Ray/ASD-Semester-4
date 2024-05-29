def subset_sum_greedy(numbers, target_sum):
    # Сортировка чисел по убыванию
    numbers.sort(reverse=True)

    subset = []
    current_sum = 0

    # Выбор чисел для подмножества
    for num in numbers:
        if current_sum + num <= target_sum:
            subset.append(num)
            current_sum += num

    return subset, current_sum

# Пример использования
numbers = [3, 34, 4, 12, 5, 2]
target_sum = 9

subset, sum_value = subset_sum_greedy(numbers, target_sum)

if sum_value == target_sum:
    print(f"Найдено подмножество с суммой {target_sum}: {subset}")
else:
    print(f"Не удалось найти подмножество с суммой {target_sum}")
    print(f"Ближайшее найденное подмножество: {subset}")
    print(f"Сумма найденного подмножества: {sum_value}")
