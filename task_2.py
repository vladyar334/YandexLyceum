def combinations(k, m, n):
    pool = tuple("a" * k + "b" * m + "c" * n)
    n = len(pool)
    indices = list(range(4))
    _ = tuple(pool[i] for i in indices)
    count = 0
    if 'a' in _ and 'b' in _ and 'c' in _:
        count += 1
    while True:
        for i in reversed(range(4)):
            if indices[i] != i + n - 4:
                break
        else:
            return count
        indices[i] += 1
        for j in range(i + 1, 4):
            indices[j] = indices[j - 1] + 1

        _ = tuple(pool[i] for i in indices)
        if 'a' in _ and 'b' in _ and 'c' in _:
            count += 1


print(combinations(*[int(i) for i in input().split(" ")]))
