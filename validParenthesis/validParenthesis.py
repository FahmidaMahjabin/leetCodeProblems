class Solution:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack) < 1:
            return "no element"
        else:
            lastItem = self.stack[-1]
            self.stack.pop(-1)
            return lastItem
        
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        for parenthesis in s:
            if parenthesis == "(" or parenthesis == "{" or parenthesis == "[":
                self.push(parenthesis)
            else:
                lastItem = self.pop()
                print("lastItem in parenthesis", lastItem)
                if lastItem == "(" and parenthesis != ")":
                    return False
                elif lastItem == "{" and parenthesis != "}":
                    return False
                elif lastItem == "[" and parenthesis != "]":
                    return False    
                else:
                    return True

parenthesis = Solution()
print(parenthesis.isValid("(]"))
