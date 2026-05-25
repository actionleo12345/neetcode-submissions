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

        max_n_room = 0
        cur_n_room = 0

        start_i = 0
        end_i = 0
        while start_i < len(intervals):
            if start_list[start_i] < end_list[end_i]:
                cur_n_room += 1
                start_i += 1
            
            else:
                cur_n_room -= 1
                end_i += 1
            
            max_n_room = max(max_n_room, cur_n_room)

        return max_n_room