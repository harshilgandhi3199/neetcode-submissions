"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # sort by start time
        intervals.sort(key=lambda x: x.start)

        # min-heap
        in_use = []
        next_room_id = 1
        available = []

        heapq.heappush(in_use, (intervals[0].end, next_room_id))

        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            while in_use and in_use[0][0] <= start:
                _, room_id = heapq.heappop(in_use)
                available.append(room_id)

            if available:
                room_id = available.pop()
                heapq.heappush(in_use, (end, room_id))
            else:
                next_room_id += 1
                heapq.heappush(in_use, (end, next_room_id))	

        return next_room_id
