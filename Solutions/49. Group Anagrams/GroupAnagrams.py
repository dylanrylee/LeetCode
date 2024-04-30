class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        First we initialize an empty hashmap and an empty list. Then we have a for loop that iterates through each 
        string in strs. We then initialize an empty list within this loop. We sort the current string, and if 
        the sorted string is not a key in the hashmap yet, we append the list inside the loop with the unsorted string, 
        and turn the value of the current key in the hashmap as the list. If the sorted string is already a key in the
        hashmap, then we just append the unsorted string into the list (updating the value of the sorted string as the key). 

        Time complexity: O(n * nlog(n)) 
        Space complexity: O(n^2)
        """
        hashmap = {}

        result = []
        for string in strs: 
            l = []
            sortedString = ''.join(sorted(string))
            if sortedString not in hashmap.keys():
                l.append(string)
                hashmap[sortedString] = l
            else:
                hashmap[sortedString].append(string) 
        for value in hashmap.values():
            result.append(value)
        return result        