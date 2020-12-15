def larrysArray(A):
    swaps = 0
    for i in range(len(A)):
        v = A[i]
        pos = abs(v-1 - i)
        print(f"i:{i}, v:{v}, pos:{pos}")
        swaps += pos
    print(swaps)
    if (swaps / 2) % 2 == 1:
        return "NO"
    else:
        return "YES"

tests = [
    #[[3, 1, 2], "YES"],
    #[[1,3,4,2], "YES"],
    #[[1,2,3,5,4], "NO"],
    [[1,6,5,2,3,4], "NO"]
]
for t in tests:
    input, want = t
    got = larrysArray(input)
    assert got == want, f"larrysArray({input}) == {want}, got {got}"