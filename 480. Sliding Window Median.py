# each time use binary insertion
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def insert(arr, target):
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = (l + h) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            arr = arr[0:l] + [target] + arr[l:]
            return arr

        arr = nums[:k]
        arr.sort()
        ans = []
        ans.append((arr[k // 2] + arr[k // 2 - (k % 2 == 0)]) / 2.)
        for i in range(k, len(nums)):
            arr.remove(nums[i - k])
            arr = insert(arr, nums[i])
            ans.append((arr[k // 2] + arr[k // 2 - (k % 2 == 0)]) / 2.)
        return ans


# each time use binary insertion
from heapq import *


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = [-nums[i] for i in range(k)]
        great = []
        heapify(small)
        heapify(great)
        for i in range(k // 2):
            heappush(great, -heappop(small))

        def median():
            if not k % 2:
                return (-small[0] + great[0]) / 2
            else:
                return -small[0]

        def remove(n):
            for x in small:
                if x == -n:
                    small.remove(-n)
                    heapify(small)
                    return
            for x in great:
                if x == n:
                    great.remove(n)
                    heapify(great)
                    return

        ans = [median()]
        for i in range(k, len(nums)):
            if not great or nums[i] < great[0]:
                heappush(small, -nums[i])
            else:
                heappush(great, nums[i])
            remove(nums[i - k])
            if len(small) - len(great) >= 2:
                heappush(great, -heappop(small))
            elif len(great) > len(small):
                heappush(small, -heappop(great))
            ans.append(median())
        return ans


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import bisect
        k = k if len(nums) > k else len(nums)
        aux = sorted(nums[:k])
        ans = []
        for i in range(k, len(nums)):
            # print(aux)
            if k % 2 == 0:
                ans.append((aux[k // 2 - 1] + aux[k // 2]) / 2.0)
            else:
                ans.append(aux[k // 2])

            bisect.insort(aux, nums[i])
            aux.pop(bisect.bisect(aux, nums[i - k]) - 1)

        if k % 2 == 0:
            ans.append((aux[k // 2 - 1] + aux[k // 2]) / 2.0)
        else:
            ans.append(aux[k // 2])
        return ans