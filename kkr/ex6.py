def function(x: int, A: int) -> bool:
    return (x & A != 0) and (x & 128 == 0) and (x & 311 == 0)


for A in range(5, 1000001, 5):
    RUNNING_BOOL: bool = True

    for x in range(1, 1000000):
        if not function(x=x, A=A):
            continue

        RUNNING_BOOL = False
        break

    if RUNNING_BOOL:
        print(A)
