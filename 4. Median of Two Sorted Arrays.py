from math import *


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findK(a, b, k):
            print(a, b, k)
            if not a:
                return b[k]
            if not b:
                return a[k]

            la, lb = len(a) // 2, len(b) // 2
            ma, mb = a[la], b[lb]
            if la + lb < k:
                if ma < mb:
                    return findK(a[la + 1:], b, k - la - 1)
                else:
                    return findK(a, b[lb + 1:], k - lb - 1)
            else:
                if ma > mb:
                    return findK(a[:la], b, k)
                else:
                    return findK(a, b[:lb], k)

        if (len(nums1) + len(nums2)) % 2 == 1:
            return findK(nums1, nums2, (len(nums1) + len(nums2)) // 2)
        else:
            return (findK(nums1, nums2, (len(nums1) + len(nums2)) // 2) + findK(nums1, nums2, (len(nums1) + len(nums2)) // 2 - 1)) / 2


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1], [9]))