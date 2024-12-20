class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_list = []
        my_dict = dict()
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        for i in range(k):
            max_key = max(my_dict, key=my_dict.get)
            my_dict.pop(max_key)
            my_list.append(max_key)
        
        return my_list