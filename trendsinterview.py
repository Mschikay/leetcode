#
# def Solution(A):
#     if A is None:
#         return 0
#
#     num = 0
#     for i in range(len(A)):
#         tree = A[0:i] + A[i+1:]
#         if nonDe(tree):
#             num += 1
#
#     return num
#
# def nonDe(tree):
#     if len(tree) == 1:
#         return True
#     for t in range(1, len(tree)):
#         if tree[t] < tree[t-1]:
#             return False
#     return True


def Solution(A, B):
    if not A or not B:
        return None


    alpha = {}

    for a in A:
        value = alpha.setdefault(a, 0)
        alpha[a] = value + 1
    print(alpha)
    for b in B:
        value = alpha.setdefault(b, 0)
        alpha[b] = value - 1
    total = 0
    for k, v in alpha.items():
        total += abs(v)

    return total

print(Solution("abcddd", "asdf"))