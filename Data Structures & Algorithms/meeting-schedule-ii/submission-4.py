"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x.start)
        max_room = 1
        heap = [intervals[0].end]

        for interval in intervals[1:]:
            s, e = interval.start, interval.end
            if heap[0] <= s:
                heapq.heappop(heap)
            
            heapq.heappush(heap, e)
            max_room = max(max_room, len(heap))
        
        return max_room
