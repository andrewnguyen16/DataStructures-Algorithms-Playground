# Naive Approach - O(n^2)
def maxIndexDiff(A):
    N = len(A)
    maxN = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[j] > A[i]:
                maxN = max(maxN, j - i)
    return maxN


print(maxIndexDiff([82, 63, 44, 74, 82, 99, 82]))
