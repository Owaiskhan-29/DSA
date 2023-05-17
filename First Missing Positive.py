class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        u= set(nums)
        i=1
        while True:
            if i not in u:
                return i
            i+=1