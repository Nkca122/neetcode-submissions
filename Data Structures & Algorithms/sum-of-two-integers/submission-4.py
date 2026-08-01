class Solution(object):
    def getSum(self, a, b):
        a &= 0xffffffff # 32 bit integers 
        b &= 0xffffffff

        while b:
            c = (a & b) << 1 # carry
            a = (a ^ b) & 0xffffffff # sum without carry
            b = c & 0xffffffff # keep adding the carry
        return a if a < 0x80000000 else ~(a ^ 0xffffffff)