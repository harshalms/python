# S=input()

# def braces(A):
#     arr=[]
#     for i in A:
#         # print(i)
#         if i=='(':
#             arr.append('(')
#         if i==')' and len(arr)!=0:
#             arr.pop()
#             continue
#         if len(arr) == 0 and i==')':
#             return False
#     if len(arr)==0:
#         return True
#     else:
#         return False

def check(a, b):
    if (a=='(' and b==')') or (a=='{' and b=='}') or (a=='[' and b==']'):
        # print(a, b)
        return True
    else:
        return False

def match(S):
    arr = []
    for c in S:
        if c in ['(', '{', '[']:
            arr.append(c)
            # print(arr)
            continue
        if c in [')', '}', ']']:
            if not arr:
                return False
            if not check(arr.pop(), c):
                return False
    if len(arr)==0:
        # print(arr)
        return True
    else:
        return False





Arr=[
    '()',
    '{}',
    '({[]})',
    '{())])}',
    ''
    # '))))((((',
    # '(((((())',
    # '()()()()',
    # '(((()))',
    # '(a+(b-c)',
    # '(((0)))'
]
for test in Arr:
    print(test)
    print(match(test))