class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        n=len(hours)
        for i in range(n):
            if hours[i]>=target:
                count+=1
        return count
        