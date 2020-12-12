
def solution(A):
    if not A:
        return 0
    lowest = None
    highest = None
    lowest_i = -1
    highest_i = -1
    for i in range(len(A)):
        elem = A[i]
        if lowest is None or elem < lowest:
            lowest_i = i
            lowest = elem
        if highest is None or elem >= highest:
            highest_i = i
            highest = elem
    if lowest_i <= highest_i:
        return highest - lowest
    almost_lowest = None
    for i in range(highest_i):
        elem = A[i]
        if almost_lowest is None or elem < almost_lowest:
            almost_lowest = elem
    almost_highest = None
    for i in range(lowest_i + 1, len(A)):
        elem = A[i]
        if almost_highest is None or elem > almost_highest:
            almost_highest = elem
    if almost_lowest is None:
        if almost_highest is None:
            return 0
        else:
            return almost_highest - lowest
    else:
        if almost_highest is None:
            return highest - almost_lowest
        else:
            return max(almost_highest - lowest, highest - almost_lowest)