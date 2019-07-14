class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def dfs(curr, v): # 每个结点和边被访问一次，是fully connected graph， time：V + E(即，V*(V - 1))
                            # 空间是ans加上递归的最大深度（ans里emails最长的长度）

            for j in range(len(accounts)):
                if j not in v:
                    emails = set(accounts[j][1:])
                    if emails & curr != set():
                        v.add(j)
                        curr |= emails
                        dfs(curr, v)

        v = set()
        ans = []
        for i in range(len(accounts)):
            if i not in v:
                a = accounts[i]
                name, emails = a[0], set(a[1:])
                dfs(emails, v)
                ans.append([name] + sorted(emails))
        return ans


