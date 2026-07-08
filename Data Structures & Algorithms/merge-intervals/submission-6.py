class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by start
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]

        for curr_start, curr_end in intervals[1:]:
            prev_end = merged[-1][1]

            if curr_start <= prev_end:
                merged[-1][1] = max(curr_end, prev_end)
            else:
                merged.append([curr_start, curr_end])

        return merged