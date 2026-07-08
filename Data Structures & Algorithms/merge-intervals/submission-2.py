class Solution:
    # Time - O(n log n)
    # Space - O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by their start time
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        i = 0
        
        while i < len(intervals):
            curr_start = intervals[i][0] 
            curr_end = intervals[i][1]
            while i < len(intervals) - 1 and curr_end >= intervals[i + 1][0]:      
                curr_end = max(curr_end, intervals[i + 1][1])
                i += 1
            result.append([curr_start, curr_end])   
            i += 1

        return result

