import sys
def combination(n, k):
    arr = [-1]*k
    flag = [True]*n+[False]
    x = 0
    y = 0
    res = []
    while True:
        if flag[y] and x < k:  # N皇后问题里面为什么不需要限制x的范围？
            flag[y] = False
            arr[x] = y
            x += 1
            y = y+1
            if x == k:  # forward ending
                arrr = [a+1 for a in arr]
                res.append(arrr[:])

        else:
            if y == n:
                if x == 0:  # backward ending
                    print(res)
                    return
                else:
                    x -= 1
                    y = arr[x]
                    flag[y] = True
            y += 1


if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    combination(n, k)