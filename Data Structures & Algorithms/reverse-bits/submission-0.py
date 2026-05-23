class Solution:
    def reverseBits(self, n: int) -> int:
        exp = 31; res = 0
        while n != 0:
            bit = n & 1; res += pow(2 * bit, exp)
            n >>= 1; exp -= 1
        return res