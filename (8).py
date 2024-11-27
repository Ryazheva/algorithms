#поразрядная сортировка

def counting_sort(arr, exp):
    n = len(arr)  # Длина массива
    output = [0] * n  # Вспомогательный массив для вывода
    count = [0] * 10  # Массив для подсчёта частоты цифр

    # Подсчёт частоты появления цифр в данном разряде
    for i in range(n):
        index = (arr[i] // exp) % 10  # Определение разряда числа
        count[index] += 1  # Увеличение счётчика для данной цифры

    # Накопление частот для правильного размещения элементов
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Конструирование выходной таблицы
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10  # Определение разряда числа
        output[count[index] - 1] = arr[i]  # Размещение числа в выходной таблице
        count[index] -= 1  # Уменьшение счётчика для данного разряда

    # Копирование отсортированного массива обратно в исходный
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_element = max(arr)  # Нахождение максимального элемента в массиве
    exp = 1  # Начальный разряд (единицы)

    # Сортировка по каждому разряду, начиная с единиц
    while max_element // exp > 0:
        counting_sort(arr, exp)  # Вызов функции подсчёта-сортировки для текущего разряда
        exp *= 10  # Переход к следующему разряду

# Ввод последовательности чисел
print("Введите последовательность чисел:")
numbers = list(map(int, input().strip().split()))  # Преобразование ввода в список целых чисел

# Сортировка массива методом поразрядной сортировки
radix_sort(numbers)

# Вывод отсортированного массива
print(' '.join(map(str, numbers)))