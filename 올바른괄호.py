def solution(s):
    stack=[]
    for i in s:
        if i == '(': stack.append(i)
        else:       # i=')'
            if len(stack)==0 or stack[-1]==i: return False
            stack.pop()
    if len(stack)!=0: return False
    return True


"""
***list로 stack을 구현하는 경우 push는 append로 해야한다.***

stack이 비었거나, stack 맨 위에 저장된 값이 ')'인데 ')'가 담기려는 경우는 괄호 짝이 맞지 않는다.
stack 맨 위에 저장된 값이 '('인데 ')'가 담기는 경우는 짝이 맞는다.
문자열 끝까지 작업을 했을 때 stack이 비어있지 않다면 아직 짝지어지지 않은 괄호가 있는 것이므로 짝이 맞지 않는다.
"""