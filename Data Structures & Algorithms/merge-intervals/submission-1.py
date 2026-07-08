class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by their start time
        intervals = sorted(intervals, key=lambda x: x[0])
        # [[1,3],[1,5],[6,7]]
        # curr_end = 5
        # curr_start = 1
        # next_start = 2
        # next_end = 3
        result = []
        i = 0
        
        while i < len(intervals):
            curr_start = intervals[i][0] 
            curr_end = intervals[i][1]   
            # next_start = interval[i+1][0]
            # next_end = intervals[i+1][1]
            while i < len(intervals) - 1 and curr_end >= intervals[i + 1][0]:       
                # if curr_end >= next_start:
                curr_end = max(curr_end, intervals[i + 1][1]) 
                curr_start = min(curr_start, intervals[i + 1][0]) 
                i += 1
            result.append([curr_start, curr_end])   
            i += 1

        return result

