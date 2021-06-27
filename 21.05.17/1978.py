# 소수 찾기

answer=0
N=int(input())
Num = (list(map(int, input().split())))

for i in Num:
    division = 0
    if i != 1:
        for j in range(2,i+1):
            if i%j == 0:
                division +=1
        
        if (division==1):
            answer+=1

print(answer)