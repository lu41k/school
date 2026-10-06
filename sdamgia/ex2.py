'''
В файле содержится последовательность натуральных чисел,
 каждое из которых не превышает 100000.
Определите количество троек элементов последовательности,
в которых ровно два из трёх элементов являются трёхзначными числами,
а сумма элементов тройки не больше максимального элемента последовательности,
оканчивающегося на 13.
Гарантируется, что в последовательности есть хотя бы одно число,
оканчивающееся на 13.

В ответе запишите количество найденных троек чисел,
затем максимальную из сумм элементов таких троек.

В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''




from typing import List, Tuple
from math import inf


def open_file(filename: str = "input.txt", directory: str = "files") -> List[int]:
    massive = open(file=f"{directory}/{filename}", mode="r").readlines()

    return [int(number.strip()) for number in massive]


def check_conditions(numbers: List[int], summary: int, compare_number: int) -> bool:
    if summary > compare_number:
        return False

    if [0 < number // 100 < 10 for number in numbers].count(True) != 2:
        return False

    return True


def algorithm(massive: List[int]) -> [int, int]:
    count: int = 0; max_summary: int or float = -inf; len_massive = len(massive)

    max_70_number: int = max(number for number in massive if number % 100 == 13)

    for index in range(1, len_massive - 1):
        numbers = massive[index - 1: index + 2]
        summary = sum(numbers)

        if check_conditions(numbers=numbers, compare_number=max_70_number, summary=summary):
            count = count + 1; max_summary = max(max_summary, summary)

            continue

    return count, max_summary


def main() -> None:
    massive = open_file(filename="17_2024.txt", directory=".")

    count, max_summary = algorithm(massive=massive)

    print(count, max_summary)


if __name__ == "__main__":
    main()
