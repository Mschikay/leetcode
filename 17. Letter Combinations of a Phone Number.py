class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {}
        d["2"] = "abc"
        d["3"] = "def"
        d["4"] = "ghi"
        d["5"] = "jkl"
        d["6"] = "mno"
        d["7"] = "pqrs"
        d["8"] = "tuv"
        d["9"] = "wxyz"

        def dfs(i, curr, ans):
            if i == len(digits):
                ans.append(curr)
                return
            for c in d[digits[i]]:
                dfs(i + 1, curr + c, ans)
            return

        ans = []
        dfs(0, "", ans)
        return ans