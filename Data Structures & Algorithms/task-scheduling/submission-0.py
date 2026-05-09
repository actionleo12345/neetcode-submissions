class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                # use 1 + to represent we use 1
                # since we change all count to negative
                # (Python doesn't have maxHeap, only minHeap)
                cnt = 1 + heapq.heappop(maxHeap)
                # if cnt = 0 then we don't need to add that to q
                if cnt:
                    q.append([cnt, (time + n)])
            
            # q[0][1] means the time we can put the cnt back to maxHeap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
