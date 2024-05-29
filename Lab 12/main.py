def compute_prefix_function(pattern):
    m = len(pattern)  # Длина шаблона
    prefix_function = [0] * m  # Инициализация префикс-функции нулями
    length = 0  # Инициализация переменной длины
    i = 1  # Индекс для итерации по шаблону

    while i < m:
        if pattern[i] == pattern[length]:  # Если символы равны
            length += 1  # Увеличиваем длину
            prefix_function[i] = length  # Присваиваем значение префикс-функции
            i += 1
        else:
            if length != 0:  # Если длина не равна нулю
                length = prefix_function[length - 1]  # Обновляем длину
            else:
                prefix_function[i] = 0  # Присваиваем значение префикс-функции
                i += 1

    return prefix_function

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_function = compute_prefix_function(pattern)  # Вычисление префикс-функции для шаблона
    matches = []  # Список для хранения совпадений

    i, j = 0, 0  # Индексы для итерации по тексту и шаблону
    while i < n:
        if pattern[j] == text[i]:  # Если символы совпадают
            i += 1
            j += 1

        if j == m:  # Если весь шаблон совпал
            matches.append(i - j)  # Добавляем индекс начала совпадения в список
            j = prefix_function[j - 1]  # Обновляем индекс шаблона для продолжения поиска
        elif i < n and pattern[j] != text[i]:  # Если символы не совпали
            if j != 0:  
                j = prefix_function[j - 1]  # Обновляем индекс шаблона
            else:
                i += 1

    return matches

# Считываем исходную строку из файла
with open('input.txt', 'r') as file:
    text = file.read()

# Получаем строку поиска от пользователя
pattern = input("Введите строку поиска: ")

# Вызываем функцию поиска образца в исходной строке
matches = kmp_search(text, pattern)

if matches:
    print(f"Pattern found at index/indices: {matches}")
else:
    print("Pattern not found in the text.")
