class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {}
        ans = []
        mins = float("inf")
        for i, l in enumerate(list1):
            d1[l] = i
        for j, l in enumerate(list2):
            if l in d1:
                s = j + d1[l]
                if s < mins:
                    ans = [l]
                    mins = s
                elif s == mins:
                    ans.append(l)

        return ans