def function(number: int, if_eight: bool = False, if_twelve: bool = False) -> int:
    if number == 21:
        if if_eight and not if_twelve:
            return 1

    elif number > 21:
        return 0

    if number == 8:
        if_eight = True
    if number == 12:
        if_twelve = True

    return function(number=number + 1, if_eight=if_eight, if_twelve=if_twelve) \
        + function(number=number + 3, if_eight=if_eight, if_twelve=if_twelve) \
        + function(number=number * 2, if_eight=if_eight, if_twelve=if_twelve)


answer = function(number=3)
print(answer)
