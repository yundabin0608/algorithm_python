# 별찍기 재귀
# 프렉탈은 재귀~
# if N=3  x=1,y=1 만 공백
# if N=9  x=1,y=1 / x=4,y=1 / x=7,y=1
#         x=1,y=4 / (3,3)(4,3)(5,3)(3,4)(4,4)(5,4)(3,5)(4,5)(5,5)/ x=7,y=4
#         x=1,y=7 / x=4,y=7 / x=7,y=7 즉 3으로 나눈 나머지가 1인놈들과 3으로 나눈 몫이 1인놈들
 

N=int(input())

def draw_star(n):
    
    matrix=[]
    # 한줄한줄별 삽입. ex 9이면 9줄중의 한줄+한줄+...
    for i in range(3*len(n)):
        if i//len(n)==1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i%len(n)]*3)
    return(list(matrix))

star =["***","* *","***"]
k=0

# N이 몇번 나눠지는지 확인 즉 3의 지수확인하는 과정 결과는 3의지수-1
while N!=3:
    N=int(N/3)
    k+=1

for i in range(k):
    star=draw_star(star)

for i in star:
    print(i)

print(star)
