
# 一个超时算法
class Solution:
    def longestSubstring(self, s, k):

        longest = 0

        for j in range(len(s)):
            num = {}
            numUnique = 0
            numLegal = 0
            end = -1
            for i in range(j, len(s)):
                value = num.setdefault(s[i], 0)
                if value == 0:
                    numUnique += 1
                num[s[i]] = value + 1
                if num[s[i]] == k:
                    numLegal += 1

                if numLegal == numUnique:
                    end = i

            longest = max(longest, end - j + 1)

        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestSubstring("ababbc", 2))


'''the worst case is k(branches)^d(depth)'''
from collections import defaultdict, Counter
class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        d = Counter(s)
        ch = None
        for key, v in d.items():
            if v < k:
                ch = key
                break
        if ch:
            ans = 0
            for new_s in s.split(ch):
                ans = max(ans, self.longestSubstring(new_s, k))
            return ans
        else:
            return len(s)
