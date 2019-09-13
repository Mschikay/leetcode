from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numset = defaultdict(int)
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.numset[number] += 1
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.numset.keys():
            if value - n in self.numset:
                if value - n == n and self.numset[n] == 1: continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)