class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        check = 1
        while num >= check:
            if num == check: return True
            check *= 4
        return False
