
def test(s, k, v):
    if k == 3: return
    s[k] = v
    test(s, k + 1, 3)


s = {}

test(s, 1, 2)
print(s)
