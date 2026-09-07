class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            minheap.append([math.sqrt(x**2 + y**2), [x, y]])
        

        heapq.heapify(minheap)
        print(minheap)
        temp = []
        while len(temp) < k:
            temp.append(heapq.heappop(minheap)[1])
        return temp
