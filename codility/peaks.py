

def zero_based_peaks(A):
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks.append(i)
    if not peaks:
        return []
    for i in range(len(peaks)):
        peaks[i] -= peaks[0]
    #print(f"peaks: {peaks}")
    return peaks


def check_flags(peaks, k):
    tails = []
    for i in range(len(peaks)):
        if peaks[i] < k:
            tails.append(peaks[i:])
        else:
            break
    #print(f"tails={tails}")
    for t in tails:
        flags = []
        for p in t:
            if not flags or p - flags[-1] >= k:
                flags.append(p)
                if len(flags) == k:
                    return flags
    return []



def solution(A):
    # write your code in Python 3.6
    peaks = zero_based_peaks(A)
    if not peaks:
        return 0
    for i in range(1, len(peaks) + 1):
        flags = check_flags(peaks, i)
        #print(f"i={i}, flags={flags}")
        if not flags:
            return i - 1
    return -42

tests = [
    [[1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3],
    [[1, 5, 1], 1],
]

for t in tests:
    input, want = t
    got = solution(input)
    assert got == want, f"f({input}) == {want}, but got {got}"
