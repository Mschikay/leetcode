from math import *


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findK(a, b, k):
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


from math import *


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findk(al, ah, bl, bh, k):
            if al > ah: return nums2[bl + k]
            if bl > bh: return nums1[al + k]
            am = (al + ah) // 2
            bm = (bl + bh) // 2
            if am + bm - al - bl + 1 <= k:
                if nums1[am] <= nums2[bm]:
                    return findk(am + 1, ah, bl, bh, k - (am - al + 1))
                else:
                    return findk(al, ah, bm + 1, bh, k - (bm - bl + 1))
            else:
                if nums1[am] <= nums2[bm]:
                    return findk(al, ah, bl, bm - 1, k)
                else:
                    return findk(al, am - 1, bl, bh, k)

        l1, l2 = len(nums1), len(nums2)
        k = (l1 + l2) // 2
        if (len(nums1) + len(nums2)) % 2 == 1:
            return findk(0, l1 - 1, 0, l2 - 1, k)
        else:
            return (findk(0, l1 - 1, 0, l2 - 1, k) + findk(0, l1 - 1, 0, l2 - 1, k - 1)) / 2