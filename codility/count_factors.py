import math

def factors(N):
    num = N
    factors = {}
    cur_factor = 2
    while num > 1 and cur_factor <= math.sqrt(num) + 2:
        print(num, cur_factor)
        if num % cur_factor == 0:
            factors[cur_factor] = factors.get(cur_factor, 0) + 1
            num = int(num / cur_factor)
        else:
            cur_factor += 1
    if num != 1:
        factors[num] = factors.get(num, 0) + 1
    print(f"{N} => {factors}")
    check = 1
    for k, v in factors.items():
        check *= k**v
    assert check == N, f"{check} != {N} ({N / check}"
    return factors


def solution(N):
    if N == 1:
        return 1
    result = 1
    for n in factors(N).values():
        result *= (n + 1)
    return result

tests = [
#    [2, 2],
#    [3, 2],
#    [5, 2],
#    [6, 4],
#    [8, 4],
#    [9, 3],
#    [24, 8],
#    [42, 8],
#    [4999696, 45],
    [49, 3],
]

for t in tests:
    input, want = t
    got = solution(input)
    assert got == want, f"f({input}) == {want}, but got {got}"
