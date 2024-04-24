class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        In this algorithm, we can initialize an empty hash set. Then we iterate through the nums list
        For each element within nums, if the element is inside the hashset already, then we add 
        element within the hashset. On the next iteration, if the element is indeed in the hashset, 
        then we return True. If we reach the end of the nums list, and all of the elements are not 
        in the hashset, then we return False, indicating that all of the elements are distinct.
        """
        hashset = set()
        # for each index in nums, we check if each 
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
        