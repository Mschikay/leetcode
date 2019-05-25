def Numbers(target, arr):
    if not arr: return 0

    def getLeftIndex(target):
        l, h = 0, len(arr) - 1
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return l

    def getRightIndex(target):
        l, h = 0, len(arr) - 1
        while l <=  h: # 左闭右闭
            mid = (l + h) // 2
            if arr[mid] <= target:
                l = mid + 1 # l取值范围是[0, n]
            else:
                h = mid - 1
            return l

    return getRightIndex(target)  - getLeftIndex(target)

