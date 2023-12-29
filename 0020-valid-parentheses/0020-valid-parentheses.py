class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = ['(', '[', '{']
        closing_brackets = [')', ']', '}']
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or bracket_map[char] != stack.pop():
                    return False

        return len(stack) == 0
