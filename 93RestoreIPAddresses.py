import copy

class Solution:
    def restoreIpAddresses(self, str):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        length = len(str)
        if length < 4:
            return result

        for i in range(1, len(str)):
            res = []
            self.dfs(len(str), str, i, 3, '', res)
            result += res

        return list(set(result))

    def dfs(self, length, s, i, times, path, res):
        if times >= 0:
            if s and int(s[0:i]) <= 255:
                path += str(int(s[0:i]))+'.'
            else:
                return

        else:
            if s == '':
                if len(path)-4 == length:
                    res.append(path[:-1])
            return

        for j in range(1, len(s[i:])+2):
            new_times = copy.deepcopy(times) - 1
            new_path = copy.deepcopy(path)
            self.dfs(length, s[i:], j, new_times, new_path, res)