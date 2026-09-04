class Solution:
    def isPalindrome(self, s: str) -> bool:

        stack = []

        for c in s:
            if c.isalnum():
                stack.append(c.lower())
        

        for c in s:

            if c.isalnum() and stack.pop() !=c.lower():
                return False
        

        return len(stack) == 0
            


        