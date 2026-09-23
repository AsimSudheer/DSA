class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}
        for i,num in enumerate(nums):
            if target - num in prev_map:
                return [prev_map[target - num],i]
            prev_map[num] = i