# Every number can be represented
# as the sum of a power of 2 and a smaller number

# The binary representation of a power of two contains 
# only one 1, thus if we can find the number of bits in 
# i - current power of 2 (most recent power of 2) + 1 we get 
# our answer

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        current_power_of_two = 1
        for i in range(1, n + 1):
            if current_power_of_two * 2 == i:
                res[i] = 1; current_power_of_two = i
            res[i] = res[i - current_power_of_two] + 1
        return res
