class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            popped = heapq.heappop(stones)
            temp = heapq.heappop(stones)
            if popped > temp:
                popped = temp - popped
                heapq.heappush(stones, popped)
            elif popped < temp:
                popped -= temp
                heapq.heappush(stones, popped)

            print(stones)
        if len(stones) == 1:
            return stones[0] * -1
        return 0
        