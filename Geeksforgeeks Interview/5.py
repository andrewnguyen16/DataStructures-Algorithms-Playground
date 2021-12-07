def bfs(x, num):
    q = []
    q.append(num)

    while q:
        num = q.pop(0)

        if num <= x:
            print(str(num), end=" || ")
            last_dig = num % 10

            if last_dig == 0:
                q.append((num * 10) + (last_dig + 1))

            elif last_dig == 9:
                q.append((num * 10) + (last_dig - 1))

            else:
                q.append((num * 10) + (last_dig - 1))
                q.append((num * 10) + (last_dig + 1))


def printJumpingNumber(x):
    print("||", str(0), end=" || ")
    for i in range(1, 10):
        bfs(x, i)


printJumpingNumber(40)
