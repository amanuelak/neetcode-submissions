class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        prefix_sum = 0

        for i, num in enumerate(nums):

            if (S - prefix_sum - num) == prefix_sum:
                return i

            prefix_sum += num

        
        return -1
