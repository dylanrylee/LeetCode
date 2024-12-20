class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        First, we initialize an empty list. Then we iterate through the nums list, and check if
        target - current element is in the list (we only check the rest of the list, excluding the current element).
        Then we append the index in the list, and we do this for every element in the list.

        Time Complexity: O(n) -- This is because the for loop is dependent on the length of the inputted nums list.
        Space Complexity: O(n) -- This is because in the worst case, each element in nums may satisfy the 
        if condition in the for loop. So it is possible that the len(nums) == len(result) would be true.
        """
        result = []
        for i in range(len(nums)):
            number = target - nums[i]
            if number in (nums[i+1:]) or number in (nums[:i]):
                result.append(i)
        return result