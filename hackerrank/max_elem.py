import fileinput

def solution(ops):
    stack = []
    counts = {}
    maxis = []
    result = []
    for op in ops:
        if op[0] == 1:
            v = op[1]
            stack.append(v)
            counts[v] = counts.get(v, 0) + 1
            if not maxis or maxis[-1] < v:
                maxis.append(v)
        elif op[0] == 2:
            if stack:
                v = stack.pop()
                counts[v] = counts[v] - 1
                if maxis and maxis[-1] == v and counts[v] == 0:
                    maxis.pop()
        else:
            if maxis:
                result.append(maxis[-1])
    return result

ops = []
for line in fileinput.input():
    ops.append([int(x) for x in line.split()])
for n in solution(ops):
    print(n)