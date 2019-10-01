'''https://www.lintcode.com/problem/wood-cut/description'''
def woodcut(nums, k):
    # if k > sum(nums): return -1
    def getPieces(m):
        ans = 0
        for n in nums:
            ans += n // m
        return ans >= k
    l, h = 1, max(nums)
    '''
        l ranges [1, max + 1]
        h ranges [0, max]
    '''
    while l <= h:
        m = (l + h) // 2
        if getPieces(m):
            l = m + 1 # m is valid here, but l is m + 1. see explains in "book copys"
        else:
            h = m - 1   # h will always be the upper bound. because the m in here is not valid getPieces(m) < k
        print(l, h)
    return h


woodcut([124,124,124],3)