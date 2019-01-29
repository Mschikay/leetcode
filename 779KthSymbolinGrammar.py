
class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if K > pow(2, N-1):
            return None

        row = [[None] * pow(2, N)] * N

        for indexN in range(N):
            for indexK in range(pow(2, indexN)):
                print(indexN, indexK)
                if indexN == 0 and indexK == 0:
                    row[indexN][indexK] = 0
                if not indexK % 2:
                    row[indexN][indexK] = row[indexN - 1][indexK // 2]
                else:
                    row[indexN][indexK] = abs(row[indexN - 1][indexK // 2] - 1)

        return row[N - 1][K - 1]


if __name__ == "__main__":
    s = Solution()
    N = 3
    K = 3
    print(s.kthGrammar(N, K))