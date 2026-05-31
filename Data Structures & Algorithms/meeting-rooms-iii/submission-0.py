class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = [] # (end, room_number)
        count = [0] * n # count[n] means each room has been used how many times

        for start, end in meetings:
            # move finished meeting to available
            while used and start >= used[0][0]: # if the current meeting(still the earliest meeting, since we sort the meetins) start time is after or equal to the earliest end used room then we can pop that used room out and make it available
                _, room_number = heapq.heappop(used)
                heapq.heappush(available, room_number)
            
            # Case01, no room available, need to push the meeting to later time
            if not available:
                end_time, room_number = heapq.heappop(used)
                end = end_time + (end-start) # we need to know the updated end time for the postponed meeting
                heapq.heappush(available, room_number)
            
            # Case02, has room available (but no matter we have room or not we always need this ste)
            room_number = heapq.heappop(available)
            heapq.heappush(used, (end, room_number))
            count[room_number] += 1

        return count.index(max(count))