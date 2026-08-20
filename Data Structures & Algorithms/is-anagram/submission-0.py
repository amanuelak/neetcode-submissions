class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if not len(s) == len(t):
            return False


        count = {} 

        for i in range(len(s)):

            count[s[i]] = count.get(s[i], 0) + 1

            count[t[i]] = count.get(t[i], 0) - 1

        for c in count:
            if count[c] != 0:
                return False

        return True
