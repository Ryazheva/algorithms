#сортировка методом прочесывания

# Функция для сортировки методом "расческой" (comb sort)
def comb_sort(arr):
    n = len(arr)  # Определяем длину массива
    step = n      # Устанавливаем начальный шаг (gap) равным длине массива
    
    # Продолжаем цикл, пока шаг больше 1 или была произведена перестановка
    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.25)  # Уменьшаем шаг, умножая его на коэффициент 1.25
        
        flag, i = False, 0  # Сбрасываем флаг перестановок и индекс i
        
        # Проходим по массиву с шагом step
        while i + step < n:
            if arr[i] > arr[i + step]:  # Если текущий элемент больше следующего с учетом шага
                arr[i], arr[i + step] = arr[i + step], arr[i]  # Меняем местами
                flag = True  # Поднимаем флаг, чтобы показать, что была перестановка
            i += step  # Переходим к следующему элементу с учетом шага
            
    return arr  # Возвращаем отсортированный массив

# Запрашиваем ввод у пользователя
print("Введите последовательность чисел:")

# Преобразуем введённые данные в список целых чисел
numbers = list(map(int, input().strip().split()))

# Сортируем список методом "расческой"
comb_sort(numbers)

# Выводим отсортированный список, объединив элементы пробелом
print(' '.join(map(str, numbers)))
