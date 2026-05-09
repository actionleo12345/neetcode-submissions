class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN, closeN):
            if openN==closeN==n:
                res.append("".join(stack))
                return
            
            #choice01, add (
            if openN <= n:
                stack.append("(")
                backtrack(openN +1, closeN)
                stack.pop()

            #choice02, add )
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res