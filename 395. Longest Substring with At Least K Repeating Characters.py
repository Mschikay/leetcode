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