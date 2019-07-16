# This question was asked in UBER interview.
def validBrackets_length(A):
    stack = []
    result, count = 0, 0
    for i in A:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack)!=0:
            stack.pop()
            count+=2
            result = max(result, count)
        else:
            count = 0
    return result
if __name__ == "__main__":
    A = ['(((()', '()()()', '((())))))()()()()()', '(())(())()', ')())']
    for i in range(len(A)):
        print(validBrackets_length(A[i]))