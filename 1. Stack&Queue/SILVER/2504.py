# 괄호의 값

#  (,),[,] 를 이용해 괄호열이 만들어짐
# '()' 와 '[]' 는 올바를 괄호열이며 x가 올바르면 (x), [x]도 올바름
# X와 Y가 올바른 괄호열이면 XY도 올바른 괄호열임
# () 괄호열 값은 2, [] 괄호열 값은 3, (x)괄호값은 2*값x, [x]괄호값은 3*값x
# XY의 괄호값은 값X+값Y

import sys
input = sys.stdin.readline

# 맨뒤 입력 제거시 슬라이싱도 ok [:-1] 아니면 rstrip()도 가능
parentheses =list(input())
parentheses = parentheses[:-1]
stack =[]
answer = 0
error = 1

for p in parentheses:
    
    if p == "(" or  p == "[":
        stack.append(p)
        cnt = 0                # 괄호가 바로 닫기는지 체크      
    elif p == ")":
        num = 0
        while len(stack) != 0: # 스택이 있다면
            top = stack.pop()
            if top == "(":
                if cnt == 0:  # ()인 상황
                    stack.append(2)
                    cnt = 1
                    error = 0   
                else:         # (2)인 상황
                    stack.append(num * 2)
                    cnt = 1
                    error = 0
                break    
            elif top == '[':  # 괄호의 짝 맞지 않으면 종료
                print(0)
                exit(0)
            else: # 숫자       
                num += int(top)
                error = 1
        if error == 1:
            print(0)
            exit(0)
    elif p == "]":
        num = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == "[":
                if cnt == 0: 
                    stack.append(3)
                    cnt = 1
                else:
                    stack.append(num * 3)
                    cnt = 1
                error = 0
                break    
            elif top == '(':
                print(0)
                exit(0)
            else:   
                num += int(top)
                error = 1
                
        if error == 1:
            print(0)
            exit(0)    
 
for s in stack:
    if s == "(" or s == "[":
        print(0)
        exit(0)
    else:
        answer += s
print(answer)