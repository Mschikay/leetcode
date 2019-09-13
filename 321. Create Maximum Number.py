class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def getKArray(nums, k):
            l = len(nums) - k
            st = []
            for num in nums:
                while st and st[-1] < num and l > 0:
                    st.pop()
                    l -= 1
                st.append(num)
            return st[:k]

        def greater(nums1, nums2, x, y):
            while x < len(nums1) and y < len(nums2) and nums1[x] == nums2[y]:
                x += 1
                y += 1
            return y == len(nums2) or x < len(nums1) and nums1[x] > nums2[y]

        def merge(st1, st2):
            i = j = 0
            curr = []
            while i < len(st1) and j < len(st2):
                if greater(st1, st2, i, j):
                    curr.append(st1[i])
                    i += 1
                else:
                    curr.append(st2[j])
                    j += 1
            if i < len(st1):
                curr += st1[i:]
            else:
                curr += st2[j:]
            return curr

        def comp(ans, res):
            for i in range(len(ans)):
                if ans[i] > res[i]:
                    return ans
                elif ans[i] < res[i]:
                    return res
                else:
                    continue
            return ans

        ans = [0] * k
        for m in range(k + 1):
            if k - m > len(nums2): continue
            if m > len(nums1): break
            stack1, stack2 = getKArray(nums1, m), getKArray(nums2, k - m)
            res = merge(stack1, stack2)
            ans = comp(ans, res)
        return ans
