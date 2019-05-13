import sys

class Solution:
    def oddEvenJumps(self, A):
        up = [False for i in range(len(A) - 1)] + [True]
        down = [False for i in range(len(A) - 1)] + [True]

        for i in range(len(A)-2, -1, -1):

            upJump = [[], sys.maxsize]
            downJump = [[], sys.maxsize]
            for v in range(i + 1, len(A)):
                if 0 <= A[v] - A[i] < upJump[1]:
                    upJump = [[v], A[v]-A[i]]

                if 0 <= A[i] - A[v] < downJump[1]:
                    downJump = [[v], A[i] - A[v]]

            for u in upJump[0]:
                if down[u]:
                    up[i] = True
                    break

            for d in downJump[0]:
                if up[d]:
                    down[i] = True
                    break

        res = 0
        for u in up:
            if u:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.oddEvenJumps([2,3,1,1,4])