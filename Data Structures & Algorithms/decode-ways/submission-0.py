class Solution:
    def numDecodings(self, s: str) -> int:
        # base case
        if not s or s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            # single digit case
            digit = int(s[i - 1])
            if digit != 0:
                dp[i] += dp[i - 1]

            # 2 digit case
            digit = int(s[i - 2:i])
            if 10 <= digit <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]