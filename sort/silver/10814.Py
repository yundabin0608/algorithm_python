# 나이순 정렬
# 나이와 이름이 가입한 순서대로 주어지면 나이: 증가순, 나이가 같으면 먼저 가입한 사람이 순
# sort, key이용, '먼저가입한순' 을 위해 인덱스를 넣어주고 정렬에 이용했는데 그냥 아예 안써도 정답되더라

N=int(input())
boj =[]

for i in range(N):
    boj.append(list(input().split()))
    boj[i].append(i)

boj.sort(key=lambda x:(int(x[0]),int(x[2]))) # 숫자로 정렬해야하므로 int 넣어줌

for age,name,k in boj:
    print(age, name)
