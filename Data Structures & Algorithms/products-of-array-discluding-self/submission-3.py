class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)
        prefix = 1


        #calculates the pre-product before the current value

        for i in range(len(output)): #[1, 1, 2, 8]
            output[i] = prefix
            prefix *= nums[i]


        postfix = 1

        for i in range(len(output) - 1, -1, -1): #[48, 24, 12, 8]
            output[i] *= postfix
            postfix *= nums[i]

        
        return output

       

            



