def two_numbers_match_int(l: list[int], k: int) -> bool:
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == k:
                return True

    return False


l1 = [10, 15, 3, 7]
k1 = 17
print(two_numbers_match_int(l1, k1))

l2 = [11, 15, 3, 7]
k2 = 17
print(two_numbers_match_int(l2, k2))
