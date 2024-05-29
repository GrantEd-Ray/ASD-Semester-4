NO_OF_CHARS = 256  # Определение константы для количества символов в ASCII таблице

def getNextState(pat, M, state, x):
        '''
        Вычисляет следующее состояние
        '''

        # Если символ c такой же, как следующий символ в шаблоне, просто увеличиваем состояние
        if state < M and x == ord(pat[state]):  # Проверка совпадения символов
                return state+1  # Увеличение состояния на 1

        i=0
        # ns хранит результат, который является следующим состоянием

        # ns в конечном итоге содержит самый длинный префикс, 
        # который также является суффиксом в "pat[0..state-1]c"

        # Начинаем с самого большого возможного значения и 
        # останавливаемся, когда найдется префикс, который также является суффиксом
        for ns in range(state,0,-1):  # Цикл для поиска наибольшего префикса-суффикса
                if ord(pat[ns-1]) == x:  # Проверка совпадения символов
                        while(i<ns-1):  # Пока не сравнили все символы
                            if pat[i] != pat[state-ns+1+i]:  # Проверка совпадения символов в префиксе и суффиксе
                                    break
                            i+=1
                        if i == ns-1:  # Если все символы совпали
                                return ns  # Возвращаем результат
        return 0  # Если нет совпадений, возвращаем 0

def computeTF(pat, M):
        '''
        Функция строит TF-таблицу, 
        которая представляет конечный автомат для заданного шаблона
        '''
        global NO_OF_CHARS

        TF = [[0 for i in range(NO_OF_CHARS)] for _ in range(M+1)]  # Создание двумерного массива для TF-таблицы

        for state in range(M+1):  # Цикл по состояниям
                for x in range(NO_OF_CHARS):  # Цикл по символам ASCII
                        z = getNextState(pat, M, state, x)  # Получение следующего состояния
                        TF[state][x] = z  # Заполнение TF-таблицы

        return TF  # Возвращаем TF-таблицу

def search(pat, txt):
        '''
        Печатает все вхождения pat в txt
        '''
        global NO_OF_CHARS
        M = len(pat)
        N = len(txt)
        TF = computeTF(pat, M)

        # Обработка txt по FA.
        state=0  # Инициализация начального состояния FA
        for i in range(N):
                state = TF[state][ord(txt[i])]  # Обновление состояния
                if state == M:  # Если достигнуто конечное состояние
                        print(f"Образец найден по индексу: {i-M+1}")    

with open("input.txt", "r") as file:
    text = file.read()

pattern = input("Введите строку поиска: ")

search(pattern, text)
print(computeTF(pattern, 3))
