class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #         nums1.sort()
        #         res = set()

        #         def search(target):
        #             l, h = 0, len(nums1) - 1
        #             while l <= h:
        #                 mid = (l + h) // 2
        #                 if nums1[mid] == target:
        #                     return True
        #                 if nums1[mid] < target:
        #                     l = mid + 1
        #                 else:
        #                     h = mid - 1
        #             return False

        #         for n in set(nums2):
        #             if search(n):
        #                 res.add(n)

        #         return list(res)
        return list(set(nums1) & set(nums2))