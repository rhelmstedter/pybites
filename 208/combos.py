def find_number_pairs(numbers, N=10):
    pairs = []
    for i, n in enumerate(numbers):
        for m in numbers[i + 1 :]:
            if n + m == N and (n, m) not in pairs:
                pairs.append((n, m))
    return pairs
