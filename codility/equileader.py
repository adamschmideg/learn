from collections import namedtuple

def half(n):
    return int(n/2)+1

def leaders(A):
    counts = {}
    best_num = None
    nums = []
    for i in range(len(A)):
        elem = A[i]
        c = counts.get(elem, 0) + 1
        counts[elem] = c
        if c > counts.get(best_num, 0):
            best_num = elem
        if counts.get(best_num, 0) >= half(i+1):
            nums.append(best_num)
        else:
            nums.append(None)
        #print('best', best_num, counts[best_num])
    print(A, '=>', nums)
    return nums

def solution(A):
    # write your code in Python 3.6
    left = leaders(A)
    left.pop()
    A.reverse()
    right = leaders(A)
    right.pop()
    right.reverse()
    total = 0
    for i in range(len(left)):
        if left[i] is not None and left[i] == right[i]:
            total += 1
    return total

Test = namedtuple('Test', ['input', 'want'])
tests = [
    Test([4, 3, 4, 4, 4, 2], 2),
    #Test([1,2,2,1,2,2],1),
]

if __name__ == '__main__':
    for t in tests:
       got = solution(t.input)
       assert got == t.want, [got, t]

