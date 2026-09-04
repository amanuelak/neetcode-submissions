class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        

        for i, num in enumerate(nums):
            postfix = nums[-1] - num
            prefix = 0 if i == 0 else nums[i - 1]

            if postfix == prefix:
                return i

        
        return -1
        