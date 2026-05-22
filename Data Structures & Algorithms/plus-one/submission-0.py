class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        global total; global carry
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, total = divmod(digits[i] + carry, 10)
            digits[i] = total
        if carry > 0:
            digits.insert(0, carry)
        return digits
