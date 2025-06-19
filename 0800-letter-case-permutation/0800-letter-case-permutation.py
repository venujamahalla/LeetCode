class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        def backtrack(sub="", i=0):
            print("sub", sub, "i:", i)
            if len(sub) == len(s):
                res.append(sub)
                return
            if s[i].isalpha():
                backtrack(sub +s[i].swapcase(), i+1)
            backtrack(sub +s[i], i+1)  
        backtrack()
        return res
          
        