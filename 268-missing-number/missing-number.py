class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = [0] * (n+1)
        for num in nums:
            ans[num] = 1
            
        for i in range(n+1):
            if ans[i] == 0:
                return i