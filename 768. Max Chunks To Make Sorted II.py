class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # l = sorted(arr)
        # s1 = s2 = 0
        # chunks = 0
        # for i in range(len(arr)):
        #     s1 += arr[i]
        #     s2 += l[i]
        #     if s1 == s2:
        #         chunks += 1
        #         s1 = s2 = 0
        # return chunks

        laterMin = []
        m = float("inf")
        ans = 0
        for i in range(len(arr) - 1, -1, -1):
            m = min(m, arr[i])
            laterMin.append(m)
        for i in range(len(arr)):
            if laterMin[i] >= arr[i]:
                ans += 1
        return ans

