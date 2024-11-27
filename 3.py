def find_numbers(x):
    """
    Функция находит все уникальные положительные числа, которые могут быть представлены в виде произведения степеней чисел 3, 5 и 7, не превышающие заданное число x.
    :param x: Верхняя граница поиска чисел.
    :return: Список найденных чисел.
    """
    results = []  # Инициализация списка для хранения результатов

    for k in range(0, x + 1):  # Перебирает степени числа 3 (3^k)
        for l in range(0, x + 1):  # Перебирает степени числа 5 (5^l)
            for m in range(0, x + 1):  # Перебирает степени числа 7 (7^m)
                number = (3 ** k) * (5 ** l) * (7 ** m)  # Вычисление числа как произведение степеней 3, 5 и 7

                if number <= x and number > 0:  # Проверяет, чтобы число было положительным и не превышало x
                    if number not in results:  # Проверяет уникальность числа
                        results.append(number)  # Добавляет уникальное число в список результатов

    return results  # Возвращает список уникальных положительных чисел, удовлетворяющих условию


if __name__ == "__main__":
    x = int(input("Введите число x: "))  # Получение ввода от пользователя
    valid_numbers = find_numbers(x)  # Вызов функции для нахождения чисел
    print("Числа от 1 до", x, "в виде 3^K * 5^L * 7^M:", valid_numbers)  # Вывод результатов

