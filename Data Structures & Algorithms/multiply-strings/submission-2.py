def str_sum(num1 : str, num2 : str) -> str:
    return f"{int(num1) + int(num2)}"
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ptr = len(num2) - 1; global product; global carry; carry = 0; global it; res = "0"
        while ptr >= 0:
            num2_digit = int(num2[ptr]); it = "0" * (len(num2) - ptr - 1)
            for num1_digit in num1[::-1]:
                product = (int(num1_digit) * int(num2_digit)) + carry
                carry = product // 10
                product %= 10
                it = f"{product}{it}"
            ptr -= 1
            if carry:
                it = f"{carry}{it}"
            carry = 0
            res = str_sum(res, it)
        return res
        



                

        