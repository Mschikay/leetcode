class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        print(self.subarraysWithAtMostKDistinct(A, K))
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K - 1)

    def subarraysWithAtMostKDistinct(self, s, k):
        if not k: return 0
        d = collections.defaultdict(int)
        i = 0
        ans = 0
        for j in range(len(s)):
            d[s[j]] += 1
            while i < j and len(d) > k:
                d[s[i]] -= 1
                if not d[s[i]]: d.pop(s[i])
                i += 1
            ans += j - i + 1
        return ans