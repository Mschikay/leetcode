class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(i, curr, ans):
            ans.append(curr)
            for j in range(i, len(curr)):
                if curr[j].isdigit(): continue
                if curr[j].islower():
                    s = curr[:j] + curr[j].upper() + curr[j + 1:]
                    dfs(j + 1, s, ans)
                else:
                    s = curr[:j] + curr[j].lower() + curr[j + 1:]
                    dfs(j + 1, s, ans)
        ans = []
        dfs(0, S, ans)
        return ans


'''
space, 递归最大的深度是字母的数量（从算法看，左边最深）+ ans的大小
time，
                        abcd
 Abcd              aBcd            abCd             abcD
 ABcd,AbCd,AbcD

树的深度是n
形状近似于
      / \
     /   \
    /   ,    
   /  ,
  / ,
 ,
 
'''