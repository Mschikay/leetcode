# recursive
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        :type preorder: List[int]
        :rtype: bool
        """

        if len(preorder) <= 1:
            return True

        def recursive(preorder, s, e):
            if e - s <= 1:
                return True

            i = -1
            for j in range(s + 1, e + 1):
                if preorder[j] > preorder[s]:
                    i = j
                    break

            if i != -1:
                for j in range(i, e + 1):
                    if preorder[j] < preorder[s]:
                        return False
                return recursive(preorder, s + 1, i - 1) and recursive(preorder, i, e)
            else:
                return recursive(preorder, s + 1, e)

        return recursive(preorder, 0, len(preorder) - 1)


# stack
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack, max_el = [], float('-inf')
        for el in preorder:
            while stack and stack[-1] < el:
                max_el = stack.pop()
            if el > max_el:
                stack.append(el)
            else:
                return False
        return True