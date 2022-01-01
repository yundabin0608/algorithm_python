# 프린터큐 

# 프린터기는 queue의 가장 앞의 문서의 중요도 확인.
# 나머지 문서들 중 현재 문서보다 중요도가 높은게 있으면 인쇄X 가장뒤에 재배치

# 입력 : 첫줄은 문서개수(1~100), 몇번째 인쇄되었는지 궁금한 문서가 현재 몇번째 줄인지의 정수M,
#       두번째줄엔 N개 문서 중요도가 차례로 주어짐 (1~9)

TC = int(input())

for _ in range(TC):
    N,M = map(int, input().split())
    case= list(map(int, input().split()))

    check=[0 for _ in range(N)] # 체크하는 리스트, 출력하는거 1로 표시
    check[M]=1
    ans=0

    while True:
        if case[0]==max(case):
            ans+=1
            if check[0]==1:
                print(ans)
                break
            case.pop(0)
            check.pop(0)
            # 3 1 3 (3) 2 이면 3번째 3이 목표이므로 목표아니면 pop해서 내보내기
        else:
            #앞에 있는거 뒤로 붙이고 체크리스트도 동일
            case.append(case.pop(0))
            check.append(check.pop(0))

    