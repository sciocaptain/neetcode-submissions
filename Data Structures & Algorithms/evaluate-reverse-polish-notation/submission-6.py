class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        res = 0
        for token in tokens:
            if token in operators:
                two = int(stack.pop())
                one = int(stack.pop())
                if token == '+':
                    res = one + two
                elif token == '-':
                    res = one - two
                elif token == '*':
                    res = one * two
                elif token == '/':
                    res = one / two
                stack.append(res)
            else: 
                stack.append(token)
        return int(stack[-1])