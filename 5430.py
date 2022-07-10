# AC

# AC는 정수 배열에 연산을 하기 위한 언어로 R(뒤집기), D(버리기) 존재
# 함수 R : 배열에 있는 수의 순서 뒤집기
# 함수 D : 첫번째 수를 버리는 함수. 빈경우에는 에러가 발생


import sys
from collections import deque
input =sys.stdin.readline

for _ in range(int(input())):
    process = input().rstrip()
    length = int(input())
    arr = deque(input().rstrip().strip('[]').split(','))

    if length == 0 : arr = deque()
   
    rev = 0
    flag=True
    for p in process:
        if flag:
            if p =="R":
                # 시간단축을 위해 reverse 하지 않고 횟수만 셈
                # 짝수라면 그대로 => 앞의 숫자 삭제 홀수면 반대이므로 => 맨 뒤 숫자 삭제
                rev+=1
            elif p =='D':
                if arr: 
                    if rev%2 == 0:
                        arr.popleft()
                    else :
                        arr.pop()
                else :
                    flag = False
                    break

    if flag:
        if rev%2 == 0 :
            print("["+ ",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+ ",".join(arr)+"]")
    else:
        print("error")