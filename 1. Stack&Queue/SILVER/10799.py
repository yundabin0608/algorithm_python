# 쇠막대기

# 여러개 쇠막대기 절단, 쇠막대기 아래->위로 겹치고 레이저 수직발사해 자름
# 쇠막대기는 자기보다 ㅇ긴거 위에만 놓을 수 있으며 포함되지만 끝은 겹치지 않게 위치
# 자르는 레이저는 적어도 한개 존재하며 어떤 쇠막대기 양끝점과도 겹치지 않음
# 레이저는 괄호쌍으로 표현, 쇠막대기 왼쪽끝은 (, 오른쪽 끝은 )
# 잘려진 쇠막대기 조각 총 개수 구하기
import sys
input = sys.stdin.readline

b_r = list(input().rstrip())
stk = []
result =0
for i in range(len(b_r)):
    if b_r[i]=="(":
        stk.append("(")
    else: # )이 나온경우
        if b_r[i-1] =="(": # 즉 ()였다면 레이저이므로 막대꺼내 잘라
            stk.pop()
            result += len(stk)
        else:              # 막대기 끝. 
            stk.pop()
            result+=1
print(result)
#  --|--|- (여기 끄트머리 더하므로 result+1)
# ---|--|-- 
# 2개 2개  => 요렇게 레이저 자를때마다 스택 더하는부분 해당 

