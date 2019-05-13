# h, w = [int(i) for i in input().split()]
#
# rec = []
# for i in range(h):
#     rec.append([int(r) for r in input().split()])
#
# # print(h, w, rec)
# def minCnt(rec, h, width):
#     b = {}
#     w = {}
#     for i in range(h):
#         for j in range(width):
#
#             if i % 2 == 0 and j % 2 == 1:
#                 b[rec[i][j]] = 1 + b.get(rec[i][j], 0)
#             elif i % 2 == 0 and j % 2 == 0:
#                 w[rec[i][j]] = 1 + w.get(rec[i][j], 0)
#             elif i % 2 == 1 and j % 2 == 0:
#                 b[rec[i][j]] = 1 + b.get(rec[i][j], 0)
#             else:
#                 w[rec[i][j]] = 1 + w.get(rec[i][j], 0)
#
#     black = []
#     white = []
#     for k, v in b.items():
#         black.append((v, k))
#     for k, v in w.items():
#         white.append((v, k))
#
#     black.sort()
#     white.sort()
#     # print(black, white)
#     color1 = color2 = colorCnt1 = colorCnt2 = 0
#     if black[-1][0] >= white[-1][0]:
#         colorCnt1, color1 = black[-1]
#         for wh in range(len(white) - 1, -1, -1):
#             if white[wh][1] != color1:
#                 colorCnt2, color2 = white[wh]
#                 break
#     else:
#         colorCnt1, color1 = white[-1]
#         for bl in range(len(black) - 1, -1, -1):
#             if black[bl][1] != color1:
#                 colorCnt2, color2 = black[bl]
#                 break
#
#     return h * width - colorCnt1 - colorCnt2
#
#
# # h = w = 3
# # rec = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# print(minCnt(rec, h, w))

from collections import defaultdict

# N = int(input())
# p = [int(i) for i in input().split()]
# c = [int(i) for i in input().split()]


# 求白色连通块数量

N = 10
p = [0, 0, 1, 2, 0, 5, 1, 2, 3]
c = [1, 0, 0, 1, 0, 0, 1, 1, 0, 1]


def cnt(N, p, c):
    node = defaultdict(list)
    for i in range(len(p)):
        node[p[i]].append(i + 1)
        node[i + 1].append(p[i])

    def dfs(i):
        visited.add(i)
        for neighbor in node.get(i, []):
            if c[neighbor] == 0 and neighbor not in visited:
                dfs(neighbor) 

    visited = set()
    cnt = 0
    for i in range(len(c)):
        if c[i] == 0 and i not in visited:
            cnt += 1
            print(i)
            dfs(i)
    return cnt


print(cnt(N, p, c))