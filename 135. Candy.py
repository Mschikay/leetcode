class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''2 passes'''
        st = []
        res = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                res[i - 1] = max(res[i - 1], res[i] + 1)
        return sum(res)
        '''one pass, worst n^2'''
        res = [1 for i in range(len(ratings))]
        i = 1
        while i < len(ratings):
            if ratings[i] < ratings[i - 1]:
                idx = i - 1
                while i + 1 < len(ratings) and ratings[i + 1] < ratings[i]:
                    i += 1
                for x in range(i - 1, idx, -1):
                    res[x] = res[x + 1] + 1
                res[idx] = max(res[idx], res[idx + 1] + 1)
            elif ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
            i += 1
        return sum(res)