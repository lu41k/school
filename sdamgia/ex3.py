'''
Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
Назовём парой два идущих подряд элемента последовательности.

Определите количество пар, в которых один из двух элементов делится на 5,
а другой меньше среднего арифметического всех нечётных элементов последовательности.
В ответе запишите два числа: сначала количество найденных пар,
а затем — максимальную сумму элементов таких пар.
'''
from typing import List, Tuple
from math import inf


def open_file(filename: str = "input.txt", directory: str = "files") -> List[int]:
    massive = open(file=f"{directory}/{filename}", mode="r").readlines()

    return [int(number.strip()) for number in massive]


def check_conditions(numbers: List[int], compare_number: float) -> bool:
    if (numbers[0] % 5 == 0 and numbers[1] < compare_number) or (numbers[1] % 5 == 0 and numbers[0] < compare_number):
        return True

    return False


def algorithm(massive: List[int]) -> [int, int]:
    count: int = 0; max_summary: int or float = -inf; len_massive = len(massive)

    nechet_massive = [number for number in massive if number % 2 == 1]
    average_number: float = sum(nechet_massive) / len(nechet_massive)

    for index in range(1, len_massive):
        numbers = massive[index - 1: index + 1]
        summary = sum(numbers)

        if check_conditions(numbers=numbers, compare_number=average_number):
            count = count + 1; max_summary = max(max_summary, summary)

            continue

    return count, max_summary


def main() -> None:
    massive = open_file(filename="17 (1).txt", directory=".")

    count, max_summary = algorithm(massive=massive)

    print(count, max_summary)


if __name__ == "__main__":
    main()
