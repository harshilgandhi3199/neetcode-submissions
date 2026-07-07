class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        strPtr, endPtr = 0, 0
        window = set()
        result = 0

        for char in s:
            if char in window:
                while s[strPtr] != char:
                    window.remove(s[strPtr])
                    strPtr += 1
                strPtr += 1
            window.add(char)
            result = max(result, endPtr - strPtr + 1)
            endPtr += 1

        return result