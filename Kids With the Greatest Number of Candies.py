class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        result=[]
        
        for i in range(len(candies)):
            if (extra+candies[i]>=max(candies)):
                result.append(True)
            else :
                result.append(False)
        return result
