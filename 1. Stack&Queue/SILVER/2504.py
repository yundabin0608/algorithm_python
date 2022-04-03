# 괄호의 값

#  (,),[,] 를 이용해 괄호열이 만들어짐
# '()' 와 '[]' 는 올바를 괄호열이며 x가 올바르면 (x), [x]도 올바름
# X와 Y가 올바른 괄호열이면 XY도 올바른 괄호열임
# () 괄호열 값은 2, [] 괄호열 값은 3, (x)괄호값은 2*값x, [x]괄호값은 3*값x
# XY의 괄호값은 값X+값Y

import sys
input = sys.stdin.readline

# 맨뒤 입력 제거시 슬라이싱도 ok 아니면 rstrip()도 가능
parentheses = list(input())
parentheses = parentheses[:-1]
stack =[]
answer = 0

# tmp를 이용해 [3] 이나 3[]의 경우등을 계산 즉 곱셈, 덧셈
# 스택에는 (,[, 숫자들이 들어갈 수 있음
for p in parentheses:
 
    if p == ")":
        tmp = 0
        while stack:
            top = stack.pop()
            if top == "(":
                if tmp == 0:  # 괄호가 바로 닫길경우
                    stack.append(2)
                else:          # 괄호 안에 숫자가 있는 경우
                    stack.append(2 * tmp)
                break
            elif top == "[":
                print("0")
                exit(0)
            
            # 숫자의 경우 숫자가 하나뿐이라면 tmp는 그 숫자, 하나 이상이면 그 숫자들을 더할 것
            # 예로 스택에 (3 일때 top=3, tmp = 3
            # 예로 스택에 ( 2 9 일때 top=9, tmp = 9 -> top=2 tmp=9+2
            else: 
                if tmp == 0:   
                    tmp = int(top)
                else:         
                    tmp = tmp + int(top)
 
    elif p == "]":
        tmp = 0
 
        while stack:
            top = stack.pop()
            if top == "[":
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if tmp == 0:
                    tmp = int(top)
                else:
                    tmp = tmp + int(top)
 
    else:  # 입력이 (나[
        stack.append(p)
 
for s in stack:
    if s == "(" or s == "[":
        print(0)
        exit(0)
    else:
        answer += s
 
print(answer)