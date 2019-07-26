class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        l = 0
        ans = ""
        for w in d:
            i = j = 0
            while i < len(s) and j < len(w):
                while i < len(s) and s[i] != w[j]:
                    i += 1
                while i < len(s) and j < len(w) and s[i] == w[j]:
                    i += 1
                    j += 1
            if j >= len(w):
                if len(w) > l:
                    l = len(w)
                    ans = w
                elif len(w) == l:
                    ans = min(w, ans)
        return ans


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort()  # Alphabetize
        d.sort(key=len, reverse=True)  # Sort by descending length order

        for w in d:
            i = j = 0
            while i < len(s) and j < len(w):
                while i < len(s) and s[i] != w[j]:
                    i += 1
                while i < len(s) and j < len(w) and s[i] == w[j]:
                    i += 1
                    j += 1
            if j >= len(w):
                return w
        return ""