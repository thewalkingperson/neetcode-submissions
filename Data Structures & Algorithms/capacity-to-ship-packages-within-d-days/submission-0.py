class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        result = right

        def canShip(cap):
            currentCap = cap
            ships = 1
            for w in weights:
                if currentCap - w < 0:
                    ships += 1
                    currentCap = cap
                currentCap -= w
            if ships > days:
                return False
            return True
                

        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result
            

        