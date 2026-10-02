class Solution:
    def isValid(self, s: str) -> bool:
        stck = list()
        braces = {'(': ')', '{': '}', '[': ']'}
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        if len(s) <= 1:
            return False
        for c in s:
            # print(stck)
            if c in opening:
                stck.append(c)
            elif c in closing and len(stck) > 0:
                pc = stck.pop()
                # print("popped", pc)
                if c != braces.get(pc):
                    return False
            else:
                return False
        if len(stck) != 0:
            return False
        return True
        