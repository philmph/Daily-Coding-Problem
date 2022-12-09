def strip_negatives_in_list(l: list[int]) -> list[int]:
    return [i for i in l if i >= 0]


def find_missing_positiv_int(l: list[int]) -> int:
    # Note: Not required to be done since we go 1++ anyway
    # we can just ignore < 0 values
    l = set(strip_negatives_in_list(l))

    for i in range(1, max(l)):
        if i not in l:
            return i

    return max(l) + 1


print(find_missing_positiv_int([3, 4, -1, 1]))
print(find_missing_positiv_int([1, 2, 0]))
