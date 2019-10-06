d = {}
m = None
route = None
longest = -1
longestPath = None

def findMax(a, b, distance):
    global m, route, longest, longestPath
    longest = -1
    longestPath = None
    if not a in d or not b in d:
        d[a].append((b, distance))
        d[b].append((a, distance))
    elif not a in d:
        s = 0
        v = set()
        path = []
        findPath(b, path, v, s)
        curr = distance + longest
        if curr > m:
            m = curr
            route = [a] + longestPath
    elif not b in d:
        s = 0
       [] v = set()
        path = []
        findPath(a, path, v, s)
        curr = distance + longest
        if curr > m:
            m = curr
            route = [b] + longestPath
    else:
        s1 = s2 = 0
        v = set()
        path1 = []
        path2 = []
        findPath(a, path1, v, s1)
        curr = distance + longest
        longest = -1
        longestPath = None
        findPath(b, path2, v, s2)
        currPath = longestPath[::-1]
        currPath += longestPath
        if curr > m:
            m = curr
            route = currPath
    return route, m


def findPath(node, path, v, s):
    global longest, longestPath
    end = True
    for n, mile in d[node]:
        if n not in v:
            end = False
            v.add(n)
            findPath(n, path + n, v, s + mile)
            v.remove(n)
    if end:
        if s > longest:
            longest = s
            longestPath = path
    return
