class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = []
        count = Counter(tasks)

        maxheap = [-c for c in count.values()]
        time = 0
        print(maxheap)
        while len(maxheap) > 0 or len(queue) > 0:
            if maxheap:
                temp = heapq.heappop(maxheap)
                temp += 1
                if temp < 0:
                    queue.append([temp, time + n])
            
            while len(queue) > 0 and queue[0][1] <= time:
                heapq.heappush(maxheap, queue.pop()[0])
            print(maxheap)
            print(queue)
            time += 1
        
        return time
