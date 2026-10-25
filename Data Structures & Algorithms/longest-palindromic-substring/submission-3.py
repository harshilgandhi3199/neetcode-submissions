# example: "abcejecfthhtfcq" output: "cfthtfc"
# abba a
# ababd
# curr_str = 'a'
# longest_str = 'a'
# left = 0
# right = 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        longest_str = ""
        for i in range(len(s)):
            # odd case
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest_str):
                    longest_str = s[left:right + 1]
                left -= 1
                right += 1

            # even case
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest_str):
                    longest_str = s[left:right + 1]
                left -= 1   
                right += 1
        
        return longest_str