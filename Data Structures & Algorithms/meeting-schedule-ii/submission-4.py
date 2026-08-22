"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sweep line
        mp = {}
        for interval in intervals:
            mp[interval.start] = mp.get(interval.start, 0) + 1
            mp[interval.end] = mp.get(interval.end, 0) - 1

        prev = 0
        res = 0

        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(prev, res)

        return res