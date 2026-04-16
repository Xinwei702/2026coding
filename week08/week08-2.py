#week08-2.py
#374. Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 二分搜尋法
        left, right = 1, n + 1  # 右邊界設為 n+1（左閉右開）
        while left < right:
            mid = (left + right) // 2  # 取中間值
            if guess(mid) == 0:
                return mid  # 猜中
            elif guess(mid) > 0:
                left = mid + 1  # 答案在右邊
            else:
                right = mid  # 答案在左邊（不包含 mid）
        return left
