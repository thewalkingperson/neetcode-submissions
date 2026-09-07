class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            #if self.timemap[key].append([timestamp, value])
            self.timemap[key].append([timestamp, value])
        else:
            self.timemap[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.timemap)
        if key in self.timemap:
            left = 0
            right = len(self.timemap[key]) - 1
            next_emotion = ""
            mid = (right + left) // 2
            while left <= right:
                mid = (right + left) // 2
                if self.timemap[key][mid][0] == timestamp:
                    return self.timemap[key][mid][1]
                elif self.timemap[key][mid][0] < timestamp:
                    next_emotion = self.timemap[key][mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
            return next_emotion
        else:
            return ""
        
