# 좌표 정렬하기 2
# y증가하는 순으로 y좌표 같으면 x증가하는 순으로 정렬

# 키정렬! sort 함수와 reverse, key=lamda 가 포인트!!

N=int(input())
loc=[]

for _ in range(N):
    loc.append(list(map(int, input().split())))

loc.sort(reverse=False, key=lambda x: (x[1], x[0])) # 우선 고려할 사항 순으로 작성

for x,y in loc:
    print(x,y)
