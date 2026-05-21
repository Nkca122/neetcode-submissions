def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack, token)
            if is_number(token):
                stack.append(int(token))
            else:
                a, b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(b+a)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(b*a)
                elif token == "/":
                    stack.append(int(b/a))
        return stack[0]