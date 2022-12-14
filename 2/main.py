import math


def product_of_list(l: list[int]) -> int:
    sum = 1
    for i in l:
        sum *= i
    return sum


def replace_index_with_product_of_list(l: list[int]) -> list[int]:
    output = []

    for i in range(0, len(l)):
        before = l[:i]
        after = l[i + 1:]
        # output.append(math.prod(before + after))
        output.append(product_of_list(before + after))

    return output


print(replace_index_with_product_of_list([1, 2, 3, 4, 5]))
print(replace_index_with_product_of_list([1, 2, 3]))
