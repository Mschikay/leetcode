from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        sd = defaultdict(lambda: 0)
        gd = defaultdict(lambda: 0)
        for i in range(len(secret)):
            sd[secret[i]] += 1
            gd[guess[i]] += 1
            if secret[i] == guess[i]: bull += 1

        for k in sd.keys():
            cow += min(sd[k], gd[k])

        return str(bull) + "A" + str(cow - bull) + "B"


from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)