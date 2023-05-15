class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li=[]
        s=sorted(nums)
        for i in nums:
            li.append(s.index(i))
        return li
