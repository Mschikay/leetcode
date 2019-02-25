# a very time consuming method:
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = []
        subProduct = 1
        res = 0

        for n in range(len(nums)):
            if n > 0 and nums[n] < k:
                res += 1

            subProduct *= nums[n]
            if subProduct < k:
                res += 1

            for p in range(0, len(product) - 1):
                if subProduct < k * product[p]:
                    res += 1
            product.append(subProduct)

        return res


# best way
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        try:
            assert nums is not None and len(nums) > 0 and k >= 1
        except:
            return 0

        l = r = res = 0
        product = 1

        while r < len(nums):
            if product < k:
                product *= nums[r]
            r += 1
            while product >= k and l < r:
                product /= nums[l]
                l += 1
            res += r - l

        return res
