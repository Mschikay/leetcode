def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if not t or not s:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while r < len(s):

        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# my solution
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        tN = Counter(t)
        uniqueN = len(tN)
        curN = defaultdict(int)
        done = 0
        res = (float("inf"), 0, 0)

        while r < len(s):
            a = s[r]
            curN[a] += 1
            if a in tN and curN[a] == tN[a]:
                done += 1
            while l <= r and done == uniqueN:
                if r - l + 1 < res[0]:
                    res = (min(res[0], r - l + 1), l, r)
                # print(res, s[res[1]:res[2] + 1])
                b = s[l]
                if b in tN and curN[b] > tN[b] or b not in tN:
                    pass
                else:
                    done -= 1
                curN[b] -= 1
                l += 1

            r += 1
        # print(res)
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]



# faster
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        tN = Counter(t)
        uniqueN = len(tN)
        curN = defaultdict(int)
        done = 0
        res = (float("inf"), 0, 0)

        filterN = []
        for i, v in enumerate(s):
            filterN.append((i, v))

        while r < len(filterN):
            a = filterN[r][1]
            curN[a] += 1
            if a in tN and curN[a] == tN[a]:
                done += 1
            while l <= r and done == uniqueN:
                if r - l + 1 < res[0]:
                    res = (min(res[0], r - l + 1), l, r)
                # print(res, s[res[1]:res[2] + 1])
                b = filterN[l][1]
                if b in tN and curN[b] > tN[b] or b not in tN:
                    pass
                else:
                    done -= 1
                curN[b] -= 1
                l += 1

            r += 1
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]