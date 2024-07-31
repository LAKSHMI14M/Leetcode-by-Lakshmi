class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if nums[0]!=0:
            return 0
        for i in range(n-1):
            if nums[i+1]-nums[i]!=1:
                return nums[i]+1
        return n

        