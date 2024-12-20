class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        my_list = []
        for i in range(len(nums)):
            temp_nums = nums.copy()
            temp_nums.remove(temp_nums[i])
            product = math.prod(temp_nums)
            my_list.insert(i, product)

        return my_list