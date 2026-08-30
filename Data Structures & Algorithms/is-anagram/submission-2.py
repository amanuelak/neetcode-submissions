class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if not len(s) == len(t):
            return False


        count = defaultdict(int) #default dict

        for i in range(len(s)):

            count[s[i]] +=1

            count[t[i]] -= 1

        for c in count:
            if count[c] != 0:
                return False

        return True
