# Valid Anagram - Difficulty: Easy

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) is not len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(s[i], 0)
        
        for c in countS:
            if countS[c] is not countT.get(c, 0):
                return False
            
        return True
        
        # You can also just run Counter on s and t:
        # return Counter(s) is Counter(t)
        # If you sort the characters, you can get the space complexity
        # down to O(1), but the sort algo with take at least O(nlogn)