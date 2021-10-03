# 홀수 홀릭 호석

# 호석이는 가지고 있는 수 N을 일련의 연산을 거치면서, 등장하는 숫자들에서 홀수를 최대한 많이 많이 보고싶음
# 수의 각 자리 숫자 중에서 홀수의 개수를 종이에 적기
# 수가 한 자리이면 종료.
# 수가 두 자리이면 2개로 나눠서 합을 구하여 새로운 수로 생각.
# 수가 세 자리 이상이면 임의로 끊어 3개의 수로 분할하고, 3개를 더한 값을 새로운 수로 생각.
# 최종값중 최대랑 최소값구하기

import math

N=input()
min_answer=math.inf  # 무한대 표시법
max_answer=0
count=0

def counting(n):
    global count
    for i in n:
        if int(i)%2 !=0 :
            count+=1
    return count

def divide(n, count):
    global min_answer,max_answer

    if len(n)==1:
        if int(n)%2!=0: count+=1
        min_answer=min(min_answer, count)
        max_answer=max(max_answer,count)
    elif len(n)==2:
        x,y = int(n[0]), int(n[1])
        tmp = str(x+y)
        divide(tmp, count+counting(tmp))
    else:
        for k in n:
            if int(k)%2!=0: count+=1
        for i in range(len(n)-2):
            for j in range(i+1, len(n)-1): # 반복문돌면서 삼등분 여러개
                a,b,c = int(n[:i+1]), int(n[i+1:j+1]), int(n[j+1:])
                tmp = str(a+b+c)
                divide(tmp, count+counting(n))
        
# 3등분을 하는게 포인트! => 그래서 입력을 string으로 받음

divide(N, counting(N))
print(min_answer, max_answer)