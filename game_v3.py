"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50  # начальное предположение
    step = 50  # начальный шаг

    while True:
        count += 1
        if predict_number == number:
            break
            
        if predict_number < number:
            predict_number += step
        else:
            predict_number -= step
            
        step = max(1, step // 2)  # уменьшаем шаг, но не меньше 1

    return count


def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict)