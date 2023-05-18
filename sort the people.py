class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        r=sorted(heights,reverse=True)
        j=0
        ans=[None]*len(names)
        for i in r:
            ans[j]=names[heights.index(i)]
            j+=1
        return ans


            
