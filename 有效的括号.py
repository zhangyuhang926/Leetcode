def isValid(s):
    if not s or len(s)%2 == 1:
        return False

    dic = {'(': ')', '[': ']', '{': '}', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1

print(isValid("(){}[]"))