class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Algorithm Description:
            initialize an empty dict. iterate through the inputted nums list. If current element i is
            not in the keys section of the dictionary, let the count (value) of that element be 1. If
            current element i is already in the keys section of the dictionary, then increment the count
            (value) of that element by 1. We then sort this dictionary where the values are in
            decreasing order.
        Time Complexity:
            O(len(nums) * m) + O(m log m), where n is the length of nums and m is the number of unique
            elements in my_dict, due to the O(n) check for key existence and the sorting operation.
        Space Complexity:
            The space complexity is O(m), as the dictionary and sorted dictionary store up to m unique
            key-value pairs. The primary computational cost comes from checking for key existence within
            a potentially large set of keys and sorting the dictionary items by their values.
        """

        my_dict = dict()

        for i in nums:
            if i not in my_dict.keys():
                my_dict[i] = 1
            elif i in my_dict.keys():
                my_dict[i] += 1
        sorted_dict = {n: v for n, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
        
        return list(sorted_dict.keys())[:k]

        