class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Pre-fix
        #Post-fix
        
        res = [1] * len(nums)
        
        #Forwards
        for i in range(1, len(nums)):
            res[i] *= nums[i-1] * res[i-1]
        
        #Backwards
        for i in range(len(nums)-1, 0, -1):
            res[i-1] *= nums[i]
            nums[i-1] *= nums[i]

        return res 