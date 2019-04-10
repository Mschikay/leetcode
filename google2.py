#字符串中最长的只包含最多两个不同字符的substring


class Solution:
    def longestMax2DiffAlphabetSubString(self, str):
        if len(str) <= 2:
            return str

        dp = [[0 for i in range(len(str))] for j in range(len(str))]
        maxDis = 2
        start = 0
        end = 1

        for i in range(2, len(str)):
            alpha = set()
            for j in range(i, -1, -1):
                alpha.add(str[j])
                if i - j <= 1:
                    continue
                else:
                    if len(alpha) == 2:
                        if str[j] not in alpha:
                            break
                        else:
                            dis = i - j + 1
                            if dis > maxDis:
                                maxDis = dis
                                start = j
                                end = i


        return maxDis, str[start:end+1]


if __name__ == "__main__":
    s = Solution()
    print(s.longestMax2DiffAlphabetSubString("abcddddddddddbcffffffddddcba"))
