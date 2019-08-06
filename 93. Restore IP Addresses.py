class Solution:
    def restoreIpAddresses(self, string):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(string) > 12: return []

        def dfs(i, curr, ans):
            if len(curr) == 4 and i == len(string):
                ans.append(".".join(curr))
                return
            if i == len(string): return
            if string[i] == "0":
                dfs(i + 1, curr + ["0"], ans)
            else:
                for j in range(i + 1, len(string) + 1):
                    if int(string[i:j]) > 255: break
                    dfs(j, curr + [str(int(string[i:j]))], ans)
            return

        ans = []
        dfs(0, [], ans)
        return ans