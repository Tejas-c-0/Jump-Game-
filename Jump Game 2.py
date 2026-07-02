class Solution(object):
    def jump(self, nums):
        left = 0
        right = 0
        jumps = 0
        while right < len(nums) - 1:
            farest = 0
            for i in range(left, right + 1):
                farest = max(farest , i + nums[i])
            left = right + 1
            right = farest

            jumps += 1
        return jumps        
        
