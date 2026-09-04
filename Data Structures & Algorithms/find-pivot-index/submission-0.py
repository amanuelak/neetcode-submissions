class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_arr = []
        total = 0

        for num in nums:
            total +=num
            prefix_arr.append(total)



        for i, num in enumerate(prefix_arr):

            postfix = prefix_arr[-1] - num
            prefix =  0 if i == 0 else prefix_arr[i - 1]

            if postfix == prefix:
                return i
        

        return -1
        