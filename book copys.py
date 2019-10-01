def copy(arr, k):
    def cost(m):
        ans = 1
        time = m
        for n in arr:
            if time < n:
                ans += 1
                time = m
            time -= n
        return ans > k

    l, h = max(arr), sum(arr)
    while l <= h:
        m = (l + h) // 2
        if cost(m):  # >m
            l = m + 1   # l is sure to be the valid range's lower bound
        else:
            # cost(m) is <= k, so after move h, the h could be less than the valid upper bound,
            # like m is valid upper bound, but h = m - 1
            # if m is also the lower bound, the h will be out of valid range!
            # so the final result should be l not h
            h = m - 1
    print(l)
    return l

copy([2, 2, 2], 3)
