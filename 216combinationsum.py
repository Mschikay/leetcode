def solve(k, n):
    x = 0
    y = 1
    item = [0] * k
    used = [False] + [True]*n + [False]*2
    res = []

    while True:
        print(x, y)

        if used[y] and x < k:
            used[y] = False
            item[x] = y
            x += 1
            y += 1
            if x == k:
                if sum(item) == n:
                    res.append(item[:])
        else:
            if y >= n:
                if x > 0:
                    x -= 1
                    y = item[x]
                    if x == 0 and y > n/k:
                        print(res)
                        return
                    used[y] = True
            y += 1


# 遇到有数字的，可以不用数组
def solve1(k, n):
    result = []

    def search(remain, stack, start):
        if remain == 0 and len(stack) == k:
            print(stack)
            result.append(stack)
            return
        # has implied that remain==0 and length < k or remain > 0 and length == k or length != k
        if remain == 0 or len(stack) >= k:
            return

        for i in range(start, 10):
            if i > n or (len(stack) > 0 and stack[0] > n/k):
                break
            search(remain-i, stack+[i], i+1)
    search(n, [], 1)
    print(result)


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(num, iterK, remainN, path):
            if iterK == k:
                if not remainN:
                    result.append(path)
                return

            for i in range(num, 10):
                if remainN < i:
                    break
                dfs(i + 1, iterK + 1, remainN - i, path + [i])
            return

        dfs(1, 0, n, [])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 9))

