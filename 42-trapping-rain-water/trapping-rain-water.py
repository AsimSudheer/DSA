class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_wall = 0
        r_wall = 0
        max_left = [0]*n
        max_right=[0]*n
        sum = 0
        for i in range(n):
            j = -i-1
            l_wall = max(l_wall,height[i])
            r_wall = max(r_wall,height[j])
            max_left[i] = l_wall
            max_right[j] = r_wall
        
        for i in range(n):
            pot = min(max_left[i],max_right[i])
            sum += max(0,pot-height[i])
        return sum