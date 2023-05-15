class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li=[""]*len(s)
        a=""
        for i in range(len(indices)):
            li[indices[i]]=s[i]
        for j in li:
            a+=''.join(j)
        return a
           
