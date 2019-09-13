class Solution:
    def partition(self, s: str) -> List[List[str]]:

        boolean = [[False for i in range(len(s))] for j in range(len(s))]

        def getPalindrome():
            for i in range(len(boolean)):
                for j in range(i, -1, -1):
                    if s[i] == s[j]:
                        if i - j <= 2:
                            boolean[j][i] = True
                        else:
                            boolean[j][i] = boolean[j + 1][i - 1]
            return

        getPalindrome()
        ans = []

        def dfs(i, curr, ans):
            if i == len(s):
                ans.append(curr)
                return
            for j in range(i + 1, len(s) + 1):
                if boolean[i][j - 1]:
                    dfs(j, curr + [s[i:j]], ans)
            return

        ans = []
        dfs(0, [], ans)
        return ans