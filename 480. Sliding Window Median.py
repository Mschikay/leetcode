# each time use binary insertion
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(arr):
            if k % 2:
                return float(arr[k // 2])
            else:
                return (arr[k // 2] + arr[k // 2 - 1]) / 2

        def insert(arr, target):
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = (l + h) // 2
                if arr[mid] <= target:
                    l = mid + 1
                else:
                    h = mid - 1
            arr = arr[0:l] + [target] + arr[l:]
            return arr

        arr = nums[:k]
        arr.sort()
        ans = []
        ans.append(median(arr))
        for i in range(k, len(nums)):
            arr.remove(nums[i - k])
            arr = insert(arr, nums[i])
            ans.append(median(arr))
        return ans

