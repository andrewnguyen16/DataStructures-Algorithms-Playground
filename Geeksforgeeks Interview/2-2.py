# Efficient Approach - O (nlog(n))
def maxIndexDiff(A):
    N = len(A)
    dct = dict()

    for i in range(N):
        if A[i] in dct:
            dct[A[i]].append(i)
        else:
            dct[A[i]] = [i]

    A.sort()
    maxDiff = 0
    temp = 1e5

    for i in range(N):
        first = dct[A[i]][0]
        last = dct[A[i]][-1]
        if temp > first:
            temp = first
        maxDiff = max(maxDiff, last)
    return maxDiff


print(maxIndexDiff([82, 63, 44, 74, 82, 99, 82]))
