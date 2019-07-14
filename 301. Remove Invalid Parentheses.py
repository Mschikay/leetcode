class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(parentheses):
            i = 0
            for p in parentheses:
                if p == "(":
                    i += 1
                elif p == ")":
                    i -= 1
                    if i < 0: return False
                else:
                    continue
            if not i:
                return True
            else:
                return False

        def dfs(idx, right, left, curr, ans):
            if not right and not left:
                if isValid(curr):
                    ans.append(curr)
                else:
                    return

            if right: # 如果先删除左边，那么在")("的情况下，删掉"("之后，指针往右边寻找，多的")"就不会管了。这样就无法添加""到ans
                for i in range(idx, len(curr)):
                    if curr[i] == ")":
                        if i > idx and curr[i] == curr[i - 1]: continue
                        dfs(i, right - 1, left, curr[:i] + curr[i + 1:], ans)
            elif left:
                for i in range(idx, len(curr)):
                    if curr[i] == "(":
                        if i > idx and curr[i] == curr[i - 1]: continue
                        dfs(i, right, left - 1, curr[:i] + curr[i + 1:], ans)
            return

        left = right = 0
        for ss in s:
            if ss == "(":
                left += 1
            elif ss == ")":
                if left:
                    left -= 1
                else:
                    right += 1
            else:
                continue

        ans = []
        dfs(0, right, left, s, ans)
        return ans