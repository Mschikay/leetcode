# time limit exceed
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        s = sum(A)
        st = A
        ans = 0
        while len(st) > 1:
            newst = []
            while len(st) > 1:
                x = st.pop()
                newst.append(min(x, st[-1]))
            ans += sum(newst)
            st = newst
        return (ans + s) % (pow(10, 9) + 7)


    def sumSubarrayMins(self, A):
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        '''[3, 1, 2, 4], [1, 2, 1, 1], [1, 3, 2, 1]
        [48,87,27] [1, 1, 3]
        '''
        leftNum = [1 for i in range(len(A))]
        rightNum = [1 for i in range(len(A))]

        st = []
        for i in range(len(A)):
            x = i
            while st and A[st[-1]] >= A[i]:
                x = st.pop()
            leftNum[i] = i - x + leftNum[x]
            st.append(i)
        st = []
        for i in range(len(A) - 1, -1, -1):
            x = i
            while st and A[st[-1]] > A[i]:
                x = st.pop()
            rightNum[i] = x - i + rightNum[x]
            st.append(i)
        ans = 0
        for i in range(len(leftNum)):
            ans += leftNum[i] * rightNum[i] * A[i]

        MOD = pow(10, 9) + 7
        return ans % MOD