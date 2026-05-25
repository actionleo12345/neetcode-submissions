"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_list = sorted([x.start for x in intervals])
        end_list = sorted([x.end for x in intervals])

        max_room = 0
        cur_room = 0

        s = 0
        e = 0

        while s < len(intervals):
            if start_list[s] < end_list[e]:
                cur_room += 1
                s += 1
            else:
                cur_room -= 1
                e += 1

            max_room = max(max_room, cur_room)
        return max_room
