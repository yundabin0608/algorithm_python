# 스택 수열

# 1~n의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 수열을 만들 수 있는데 스택에 push 하는 순서는 오름차순
# 임의의 수열이 주어졋을때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 가능하면 어떤순으로 push, pop
# 출력 : 수열 만들기 위해 필요한 연산 한줄 한개씩 출력 푸쉬는+ 팦은 - 불가능은 NO
# 오름차순 push인거 주의! 5push 하려면 1,2,3,4,5 넣는거임

n=int(input())
stack=[]
ans=[]
flag=0    # NO 인지 판단
current=1 # 현재 쌓아올린 수

for i in range(n):
    inNum=int(input())
    # 들어온 입력값만큼 쌓아올리고 (필요없으면 안해도 ok)
    while current <= inNum:
        stack.append(current)
        ans.append("+")
        current+=1
    # 가장 위에 있는게 목표하는 수이면 빼기
    if stack[-1]==inNum:
        stack.pop()
        ans.append("-")
    # 3을 빼야하는데 3->4 순으로 쌓인경우 st 불가 NO print
    else: 
        flag=1
        break

if flag==1:
    print("NO")
else:
    for k in ans:
        print(k)
    




# 1번예제 보면 1234(++++) 넣고 4->3 빼고(--) 56넣고 (++) 6빼고(-) 
# 78넣고(++) 8->7->5->2->1 빼기(-----)
