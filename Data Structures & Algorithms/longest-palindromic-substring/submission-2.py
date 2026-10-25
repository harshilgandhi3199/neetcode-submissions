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
            curr_str = s[i]
            # check with next char
            # even case
            if i < len(s) - 1 and s[i] == s[i + 1]:
                curr_str += s[i + 1]
                # even substring
                left = i - 1
                right = i + 2
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    curr_str = s[left:right + 1]
                    left -= 1
                    right += 1
                if len(curr_str) > len(longest_str):
                    longest_str = curr_str
            # odd case
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_str = s[left:right + 1]
                left -= 1
                right += 1
            if len(curr_str) > len(longest_str):
                longest_str = curr_str
        
        return longest_str