trie = {}
words = ['tree', 'fans', 'yogurt', 'fuel']
for w in words:
            t=trie
            for c in w:
                if c not in t:
                    t[c]={}
                t=t[c]
            t['#']='#'
print(trie)

board=[[1, 2], [2, 2]]
used = [[False] * len(board[0]) for _ in range(len(board))]
print(used)
print('#' in trie, 'u' in trie)
