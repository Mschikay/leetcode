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


from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # find root
        def findroot(i):
            if root[i] != i:
                root[i] = findroot(root[i])  # path compression
            return root[i]

        # union find
        d = {}  # key:val = email:index
        root = list(range(len(accounts)))
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in d:
                    r1, r2 = findroot(i), findroot(d[email])
                    root[r1] = r2
                else:
                    d[email] = i

        # merge accounts
        from collections import defaultdict
        res0 = defaultdict(set)  # key:val = index: {set of emails}
        for i in range(len(accounts)):
            res0[findroot(i)] |= set(accounts[i][1:])

        # convert into required format
        res = []
        for k, v in res0.items():
            res.append([accounts[k][0]] + sorted(v))

        return res