# 순화강연

# N개 대학에서 강연 요청, d일 안에 와서 강연하면 q의 강의료 지불 (N,d,q: 1~10000)
# 학자는 하루에 최대 한곳에서 강연. 최대로 벌 수 있는 돈 출력

import heapq
N=int(input())
lectures=[]

for i in range(N):
    lectures.append(list(map(int, input().split())))

# 리스트 둘째 인자를 오름차순으로 먼저 정렬 후 첫째 인자를 내림차순으로 정렬
lectures.sort(key=lambda x: (x[1], -x[0]))
tmp=[] 

for q,d in lectures:
    heapq.heappush(tmp, q)
    print("push", tmp)
    if (len(tmp)>d):
        heapq.heappop(tmp)
        print("***pop***", tmp)

print(sum(tmp))
    
#====> 여기 오답임
# for l in lectures:
#     tmp.append(l[0])
#     if (len(tmp)>l[1]):
#         tmp.pop()
# print(sum(tmp))

# PAY 의 정렬 유무
# 5
# 2 1
# 20 1
# 40 1
# 2 2
# 8 2

# (pay 정렬 X)          (pay 정렬 O)
# push [2]             push [40]
# push [2, 20]         push [20, 40]
# ***pop*** [20]       ***pop*** [40]
# push [20, 40]        push [2, 40]
# ***pop*** [40]       ***pop*** [40]
# push [2, 40]         push [8, 40]
# push [2, 40, 8]      push [2, 40, 8]
# ***pop*** [8, 40]    ***pop*** [8, 40]
