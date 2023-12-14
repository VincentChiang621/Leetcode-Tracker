class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == '+':
                stack.append(stack.pop() + stack.pop())
            elif n == '-':
                n1, n2 = stack.pop(), stack.pop()
                stack.append(n2 - n1)
            elif n == '/':
                n1, n2 = stack.pop(), stack.pop()
                stack.append(int(n2 / n1))
            elif n == '*': 
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(n))
        
        return stack[0]