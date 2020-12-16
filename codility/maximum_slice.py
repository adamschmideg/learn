def solution(A):
    # write your code in Python 3.6

    best_index = 0
    best = A[0]
    total = best
    for i in range(1, len(A)):
        elem = A[i]
        total += elem
        if total >= best:
            best_index = i
            best = total

    #print(f"{best_index}=>{best}")
    decrease = 0
    least = 0
    for i in range(0, best_index):
        decrease += A[i]
        if decrease < least:
            least = decrease
    #print(f"least: {best}, {least}", best - least, A[-1])
    return max(best - least, max(A))

tests = [
    [[3,2,-6,4,0], 5],
    [[-1, 2, 3, -2, 1], 5],
    [[-5], -5],
    [[-2, 1, 1], 2],
    [[-2, -2, 1], 1],
    [[-2, -2, 1, 1, -2, -2], 2],
    [[-2, -2, 1, -2, -2], 1],
]
if __name__ == '__main__':
    for input, want in tests:
        got = solution(input)
        assert got == want, f"{input} => {got}, not {want}"

