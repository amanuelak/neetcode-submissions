class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False


        stack = []

        for c in s:

            if c in "[({":
                stack.append(c)
            
            else:
                if not stack:
                    return False

                last = stack.pop()

                if (last == '(' and c != ')') or \
                    (last == '{' and c != '}') or \
                    (last == '[' and c != ']'):
                    return False


        return len(stack) == 0
                


