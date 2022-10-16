# 균형잡힌 세상

# 주어진 문자열의 균형을 판단
# 문자열의 괄호는 소괄호, 대괄호 2종이며 (는 )와, [는 ]와 짝을 이룰것, 오른쪼 괄호들은 자기와 짝인 왼괄호 존재
# 모든 괄호 짝은 일대일 매칭만 가능하고, 짝인 괄호 사이엔 문자열이 존재 가능
# 문자열은 100글자 이내이며 마침으로 .이 들어옴

import sys
input = sys.stdin.readline

while(True):
    string = input().rstrip()
    if string == "." : break
    string = string[:-1]
    stack = []
    flag = True

    for tmp in string:
        if tmp in "([":
            stack.append(tmp)
        elif tmp == ")":
            if stack and stack[-1] == "(": stack.pop()
            else: 
                flag = False
                break
        elif tmp == "]":
            if stack and stack[-1] == "[": stack.pop()
            else:
                flag = False
                break
    
    print("yes" if flag and not stack else "no")