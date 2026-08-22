class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}
        for char in s1:
            freq_map[char] = freq_map.get(char, 0) + 1

        start = 0
        n = len(s1)
        curr_map = {}

        for end in range(len(s2)):
            # expand our window
            curr_map[s2[end]] = curr_map.get(s2[end], 0) + 1

            # check if window is valid; if yes, compare hash maps
            if n == (end - start + 1):
                if freq_map == curr_map:
                    return True

                curr_map[s2[start]] -= 1
                if curr_map[s2[start]] == 0: del curr_map[s2[start]]
                start += 1

        return False