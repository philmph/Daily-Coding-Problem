def cons(a: int, b: int) -> tuple[int]:
    return (a, b)


def car(pair: tuple[int]) -> int:
    return (int(pair[0]))


def cdr(pair: tuple[int]) -> int:
    return (int(pair[-1]))


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
