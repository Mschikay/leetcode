from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        keys = []
        for s in strs:
            skey = "".join(sorted(s))
            for k in keys:
                if skey == k:
                    d[k].append(s)
                    continue
            d[skey].append(s)
        res = []
        for k in d.keys():
            res.append(d[k])
        return res

