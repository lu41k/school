from typing import List


def check_if_has_orientir(n: int, graph_matriza: List[List[int]]) -> bool:
    for row_index in range(n):
        for column_index in range(row_index):
            if graph_matriza[row_index][column_index] == graph_matriza[column_index][row_index]:
                continue

            return True

    return False


def get_matriza() -> [int, List[List[int]]] or None:
    n = int(input().strip())

    matriza: List[List[int]] = []

    for row in range(n):
        matriza.append(list(map(int, input().strip().split(" "))))

    if check_if_has_orientir(n=n, graph_matriza=matriza):
        print("NO")
        exit()

    return n, matriza


def alghoritm(n: int, matriza: List[List[int]]) -> int:
    count_rebra: List[int] = []

    for row in range(n):
        count: int = 0

        for column in range(n):
            if row == column:
                continue

            if matriza[row][column] == 1:
                count += 1

        count_rebra.append(count)

    return count_rebra.count(max(count_rebra))


def main() -> None:
    n, matriza = get_matriza()

    answer = alghoritm(n=n, matriza=matriza)

    print(answer)


if __name__ == "__main__":
    main()
