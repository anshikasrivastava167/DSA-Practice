class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for c in string:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        return build(s) == build(t)