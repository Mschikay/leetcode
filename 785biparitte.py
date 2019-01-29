from collections import deque


class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return None

        hash = {}
        queue = deque()

        for g in range(len(graph)):

            if graph[g] and g not in hash:
                queue.append((g, graph[g]))
                hash[g] = 1

            while queue:
                node = queue.popleft()
                tag = -1 * hash[node[0]]

                for neighbor in node[1]:
                    if neighbor not in hash:
                        queue.append((neighbor, graph[neighbor]))
                    if hash.setdefault(neighbor, tag) != tag:
                        return False

        return True


if __name__ == "__main__":
    l = [[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18], [], [16],
     [15], [23], [23], [], [20, 21], [], [], [27], [26], [], [], [34], [33, 34], [], [31], [30, 31], [38, 39],
     [37, 38, 39], [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49],
     [45, 46, 47, 48]]
    s = Solution()
    print(s.isBipartite(l))