# 요세푸스 문제

# N명의 사람들이 원을 이뤄 앉아있으며 K(<=N)번째 사람을 제거함
# 한사람이 제거되면 남은 사람들로 이뤄진 원을 따라서 계속 진행 -> N명 모두 제거될때까지
# 출력 : 요세푸스 순열

N,K=map(int,(input().split()))

people=[]
answer=[]
tmp = K-1          # 1은 배열의 0번째 2는 배열의 1번째 .. 에 있으므로 
for i in range(1,N+1): 
    people.append(i)

for x in range(N): # 사람수만큼 반복하면서 사람 꺼내야하니까

    # 위치가 리스트를 넘는지 안넘는지 체크해서 꺼내기
    if len(people)>tmp:
        answer.append(people.pop(tmp))
        tmp+=K-1
    
    else:
        tmp = tmp%len(people)
        answer.append(people.pop(tmp))
        tmp+=K-1

print("<", end='')
for i in answer:
    if i == answer[-1]:
        print(i, end = '')
    else:
        print("%s, " %(i), end='')
print(">")

