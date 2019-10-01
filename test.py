'''directed or not'''
for k, v in g.items():
    for neighbor in v:
        if k not in g[neighbor]:
            print("not directed")
print("directed")

'''largest degree'''
l = 0
node = []
for k, v in g.items():
    if l < len(v):
        l = v
        node = [k]
    elif l == len(v):
        node.append(k)
print(node)


def canVisit(node, visit):
    for n in g[node]:
        if n not in visit:
            visit.add(n)
            canVisit(n, visit)
    return


for k, v in g.items():
    visit = set()
    canVisit(k, visit)
    if len(visit) != len(g) - 1:
        print("not connected")
print("connected")