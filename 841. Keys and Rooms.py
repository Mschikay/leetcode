from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        v = set()

        q.append(0)
        while q:
            roomNum = q.pop()
            v.add(roomNum)
            for key in rooms[roomNum]:
                if key not in v:
                    q.append(key)

        return len(v) == len(rooms)


'''dfs'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def visit(roomNum, v):
            for key in rooms[roomNum]:
                if key not in v:
                    v.add(key)
                    visit(key, v)
        v = set()
        v.add(0)
        visit(0, v)
        return len(v) == len(rooms)