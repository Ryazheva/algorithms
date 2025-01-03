#сортировка вставками

print("Введите последовательность чисел:")

# Функция для сортировки методом вставки
def insertion_sort(arr):
    # Внешний цикл проходит по каждому элементу массива, начиная со второго
    for i in range(1, len(arr)):
        # Сохраняем значение текущего элемента
        key = arr[i]
        # Индекс предыдущего элемента
        j = i - 1
        
        # Внутренний цикл перемещает элементы массива вперед, 
        # пока не найдет подходящее место для текущего элемента
        while j >= 0 and key < arr[j]:
            # Перемещаем элемент вправо
            arr[j + 1] = arr[j]
            # Двигаемся назад по массиву
            j -= 1
        
        # Вставляем текущий элемент на нужное место
        arr[j + 1] = key

# Получаем ввод от пользователя, разбиваем его на список строк и преобразуем в целые числа
numbers = list(map(int, input().strip().split()))

# Вызываем функцию для сортировки массива
insertion_sort(numbers)

# Выводим отсортированный массив, объединяя элементы пробелом
print(' '.join(map(str, numbers)))

