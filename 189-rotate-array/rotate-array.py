from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k >= n
        A = [0] * n
        
        for i in range(n):
            A[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = A[i]
