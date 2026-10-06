'''
В файле содержится последовательность натуральных чисел.
Её элементы могут принимать целые значения от 1 до 100 000 включительно.

Определите количество пар последовательности,
в которых только один из элементов является двузначным числом,
а сумма элементов пары кратна минимальному двузначному элементу последовательности.

В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
from typing import List, Tuple
from math import inf


def open_file(filename: str = "input.txt", directory: str = "files") -> List[int]:
    massive = open(file=f"{directory}/{filename}", mode="r").readlines()

    return [int(number.strip()) for number in massive]


def check_conditions(numbers: List[int], summary: int, compare_number: int) -> bool:
    if summary % compare_number != 0:
        return False

    if (9 < numbers[0] < 100 and not (0 < numbers[1] // 10 < 10)) or (9 < numbers[1] < 100 and not (0 < numbers[0] // 10 < 10)):
        return True

    return False


def algorithm(massive: List[int]) -> [int, int]:
    count: int = 0; max_summary: int or float = -inf; len_massive = len(massive)

    min_number: int = min(number for number in massive if 9 < number < 100)

    for index in range(1, len_massive):
        numbers = massive[index - 1: index + 1]
        summary = sum(numbers)

        if check_conditions(numbers=numbers, compare_number=min_number, summary=summary):
            count = count + 1; max_summary = max(max_summary, summary)

            continue

    return count, max_summary


def main() -> None:
    massive = open_file(filename="DEMO_17.txt", directory=".")

    count, max_summary = algorithm(massive=massive)

    print(count, max_summary)


if __name__ == "__main__":
    main()
