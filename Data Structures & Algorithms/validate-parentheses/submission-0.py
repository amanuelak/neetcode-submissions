class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False

        if "()" in s:
            return self.isValid(s.replace("()", "", 1))
        elif "[]" in s:
            return self.isValid(s.replace("[]", "", 1))
        elif "{}" in s:
            return self.isValid(s.replace("{}", "", 1))
        else:
            return False