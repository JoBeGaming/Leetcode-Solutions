class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Get the original length of s (will be important later)

        slen = len(s)

        # [a, b, c] -> [a, b, c, c, b, a]
        for element in reversed(s):
            s.append(element)

        # [a, b, c, c, b, a] -> [c, b, a]
        del s[:slen]