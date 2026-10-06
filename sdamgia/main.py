'''
В файле содержится последовательность целых чисел. 
Её элементы могут принимать целые значения от –100000 до 100000 включительно.
Определите количество троек элементов последовательности,
в которых ни одно число не является отрицательным,
а сумма элементов тройки не больше максимального элемента последовательности,
оканчивающегося на 70.

В ответе запишите количество найденных троек, затем максимальную из сумм чисел таких троек.

В данной задаче под тройкой подразумеваются три идущих подряд элемента последовательности.
'''




from typing import List, Tuple
from math import inf


def open_file(filename: str = "input.txt", directory: str = "files") -> List[int]:
    massive = open(file=f"{directory}/{filename}", mode="r").readlines()

    return [int(number.strip()) for number in massive]


def check_conditions(numbers: List[int], summary: int, compare_number: int) -> bool:
    if summary > compare_number:
        return False

    if [number >= 0 for number in numbers].count(True) != 3:
        return False

    return True


def algorithm(massive: List[int]) -> [int, int]:
    count: int = 0; max_summary: int or float = -inf; len_massive = len(massive)

    max_70_number: int = max(number for number in massive if number % 100 == 70)

    for index in range(1, len_massive - 1):
        numbers = massive[index - 1: index + 2]
        summary = sum(numbers)

        if check_conditions(numbers=numbers, compare_number=max_70_number, summary=summary):
            count = count + 1; max_summary = max(max_summary, summary)

            continue

    return count, max_summary


def main() -> None:
    massive = open_file(filename="17.txt", directory=".")

    count, max_summary = algorithm(massive=massive)

    print(count, max_summary)


if __name__ == "__main__":
    main()
