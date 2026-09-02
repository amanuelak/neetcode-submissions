class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        if len(strs) == 0:
            return "∅"

        return "π".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        if s == "∅":
            return []

        return s.split("π")