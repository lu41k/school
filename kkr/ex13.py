from typing import List


def get_input_values(n: int) -> List[int]:
    points: List[int] = []

    for line in range(n):
        points.append(sum(int(point) for point in input().strip().split(" ")))

    return points


def sort_massive(massive: List[int]) -> List[int]:
    return sorted(massive, key=lambda x: x, reverse=True)


def get_answer(massive: List[int], sorted_massive: List[int]) -> [int, int]:
    max_points = sorted_massive[0]

    return max_points, massive.index(max_points)


def main() -> None:
    n, m = map(int, input().strip().split(" "))

    points = get_input_values(n=n)
    sorted_points = sort_massive(massive=points)

    max_points, index_sportsman = get_answer(massive=points, sorted_massive=sorted_points)

    print(max_points)
    print(index_sportsman)


if __name__ == "__main__":
    main()
