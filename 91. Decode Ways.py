class Solution:
    def numDecodings(self, s: str) -> int:
        d = {}
        d[len(s)] = 1

        def helper(idx):
            st = s[idx:]

            if idx in d.keys():
                return d[idx]
            elif not st:
                return 0
            elif st[0] == "0":
                return 0
            elif len(st) == 1:
                return 1
            else:
                num = helper(idx + 1)
                pre = st[:2]
                if int(pre) <= 26:
                    num += helper(idx + 2)
            d[idx] = num
            return num

        return helper(0)