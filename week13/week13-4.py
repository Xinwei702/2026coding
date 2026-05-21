#week13-4.py
#2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.now = 1
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            return heappop(self.heap)
        self.now += 1
        return self.now - 1

    def addBack(self, num: int) -> None:
        print("zz")
        if num < self.now:
            heappush(self.heap, num)
