import sys


class Solution:
    def find_max(self, nums):
        if not nums:
            return None

        max_num = -sys.maxsize

        for num in nums:
            if num > max_num:
                max_num = num
        return max_num


if __name__ == '__main__':
    s = Solution()
    print(s.find_max([]))