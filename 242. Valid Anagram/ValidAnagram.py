class Solution(object):
    def isAnagram(self, s, t) :
        """
        :type s: str
        :type t: str
        :rtype: bool

        First we initialize two separate empty lists. Then we check if the length of both strings are not equal,
        then they are automatically not anagrams. Otherwise, we have to check if they contain the same exact elements
        and the same number of those elements as well. We iterate through each char on both strings, and then add each 
        char in their respective list. We can use the built-in sorted Python function to sort each of the lists. Now
        we compare if the sorted lists are then equal. 

        Time Complexity: O(nlog(n))
        Space Complexity: O(|s| + |t|)
        """
        hashsetS = []
        hashsetT = []
        if (len(s) != len(t)):
            return False
        else:
            for i in s:
                hashsetS.append(i)
            for i in t:
                hashsetT.append(i)
            if (sorted(hashsetS) == sorted(hashsetT)):
                return True
            else:
                return False
        