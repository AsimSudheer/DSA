class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        amount = 0
        left=0
        right = n -1 
        while left<right:
            min_height = min(height[left],height[right])
            width= right - left
            area = min_height*width
            amount = max(amount,area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -=1

        
        '''amount = 0 #bruteforce   [O(n^2)]
        for i in range(n-1):
            for j in range(i+1,n):
                min_height = min(height[i],height[j])
                width = j-i
                area = min_height*width
                amount = max(amount,area)
                
                if height[i] <= height[j]:
                    amount = max(amount,height[i] * (j-i))
                else:
                    amount = max(amount,height[j] * (j-i))'''
            
        return amount
