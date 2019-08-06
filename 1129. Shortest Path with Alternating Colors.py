from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        paths = set()
        edge = defaultdict(list)
        for a, b in red_edges:
            paths.add((a, b, 1))
            edge[a].append(b)
        for a, b in blue_edges:
            paths.add((a, b, -1))
            edge[a].append(b)

        answer = [0] + [-1] * (n - 1)

        def search(curr, color, num):
            if answer[curr] == -1:
                answer[curr] = num
            else:
                answer[curr] = min(answer[curr], num)
            for n in edge[curr]:
                if (curr, n, -color) in paths:
                    paths.remove((curr, n, -color))
                    search(n, -color, num + 1)
                    paths.add((curr, n, -color))
            return

        search(0, 1, 0)
        search(0, -1, 0)
        return answer


from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        paths = set()
        edge = defaultdict(list)
        for a, b in red_edges:
            paths.add((a, b, 1))
            edge[a].append(b)
        for a, b in blue_edges:
            paths.add((a, b, -1))
            edge[a].append(b)

        answer = [0] + [-1] * (n - 1)
        q = deque()
        q.append((0, -1, 0))
        q.append((0, 1, 0))
        while q:
            node, color, step = q.popleft()
            if answer[node] == -1: answer[node] = step
            for n in edge[node]:
                if (node, n, -color) in paths:
                    paths.remove((node, n, -color))
                    q.append((n, -color, step + 1))
        return answer



