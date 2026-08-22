class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        start = 0
        output = 0

        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            max_freq = max(freq_map.values())

            # contract window until the window becomes valid again
            while not max_freq + k >= (end - start + 1):
                if freq_map[s[start]] > 0: freq_map[s[start]] -= 1
                start += 1
                
            # update output because window is valid
            output = max(output, end - start + 1)

        return output

            
           