def build_bad_character_table(pattern):
    # Функция для создания таблицы плохих символов
    table = {}
    for i in range(len(pattern) - 1):
        # Заполняем таблицу плохих символов, указывая смещение для каждого символа
        table[pattern[i]] = len(pattern) - 1 - i
    return table

def boyer_moore_search_all(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []  # Если длина образца равна 0, возвращаем пустой список

    bad_character_table = build_bad_character_table(pattern)  # Создаем таблицу плохих символов
    occurrences = []  # Список для хранения всех вхождений образца в текст

    i = m - 1  # Начинаем поиск с конца образца

    while i < n:
        j = m - 1
        k = i

        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1

        if j == -1:
            # Если весь образец совпал, добавляем индекс начала вхождения в список
            occurrences.append(k + 1)

        if text[i] in bad_character_table:
            i += bad_character_table[text[i]]  # Смещение согласно таблице плохих символов
        else:
            i += m  # Если символ отсутствует в таблице, смещаемся на длину образца

    return occurrences  # Возвращаем список всех вхождений образца в текст

# Чтение строки из файла
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read().strip()

pattern = input("Введите строку поиска: ")
results = boyer_moore_search_all(text, pattern)
if results:
    print(f"Pattern found at indices: {results}")
else:
    print("Pattern not found")
