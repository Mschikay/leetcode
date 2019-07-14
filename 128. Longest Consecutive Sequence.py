
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''UNION FIND'''
        if not nums: return 0

        def find(num, d):
            if num not in d:
                d[num] = num
            if num != d[num]:
                d[num] = find(d[num], d)
            return d[num]

        d = collections.defaultdict(int)
        for n in nums:
            if n in d: continue
            x = find(n, d)
            if n + 1 in d:
                d[find(n + 1, d)] = x
            if n - 1 in d:
                d[find(n - 1, d)] = x

        size = collections.Counter([find(n, d) for n in d.values()])
        print(size)
        return max(size.values())


'''set'''
class Solution:
    def longestConsecutive(self, nums):
        numset = set(nums)
        ans = 0

        for n in numset:
            if n - 1 in numset:
                continue

            curr = 0
            while n in numset:
                curr += 1
                n += 1
            ans = max(ans, curr)

        return ans