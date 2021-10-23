def subArraySum(arr, sum):
    n = len(arr)
    curr_sum = arr[0]
    first = 0
    last = 1
    while last <= n:
        while curr_sum > sum and first < last - 1:
            curr_sum = curr_sum - arr[first]
            first += 1
        if curr_sum == sum:
            return [first, last - 1]
        if last < n:
            curr_sum = curr_sum + arr[last]
        last += 1
    return -1


print(subArraySum([15, 2, 4, 8, 9, 5, 10, 23], 23))
