def UniqueNumbers2(arr):
    dct = dict()
    for i in range(len(arr)):
        if arr[i] in dct:
            dct[arr[i]] += 1
        else:
            dct[arr[i]] = 1

    result = []

    for key, value in dct.items():
        if value == 1:
            result.append(key)
    return result


print(UniqueNumbers2([2, 3, 7, 9, 11, 2, 3, 11]))
