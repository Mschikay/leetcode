class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0

        def split(nums, l, r):
            if l == r: return 0
            mid = (l + r) // 2
            cnt = split(nums, l, mid) + split(nums, mid + 1, r)

            i, j = l, mid + 1
            while i <= mid:
                while j <= r and nums[i] > nums[j] * 2:
                    j += 1
                cnt += j - mid - 1
                i += 1  # j doesn't need to start from mid + 1 again in next loop

            nums[l:r + 1] = sorted(nums[l:r + 1])
            return cnt

        return split(nums, 0, len(nums) - 1)