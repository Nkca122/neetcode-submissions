def square_sum(n : int) -> int:
    total = 0
    while n > 0:
        digit = n % 10
        total += int(pow(digit, 2))
        n //= 10
    return total
class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()
        while n != 1:
            total = square_sum(n); print(total)
            if total in sum_set:
                return False
            sum_set.add(total); print(sum_set)
            n = total
        return True

        