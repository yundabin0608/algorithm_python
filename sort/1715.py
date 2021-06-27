# 카드 정렬하기
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 
# 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성


# 숫자 카드 묶음 개수 받고 카드 묶음 크기를 리스트에 넣기

N = int(input())
bundle_size = []

for i in range(N):
    bundle_size.append(int(input()))

if N==1:
    print(0)
elif N==2:
    print(bundle_size[0]+bundle_size[1])
else:
    result=0
    while len(bundle_size) != 1:
        bundle_size.sort()
        bundle_size[0:2]=[bundle_size[0]+bundle_size[1]]
        result+=bundle_size[0]

    print(result)




# 리스트 정렬후 맨앞의 두개 꺼내서 합해준후 리스트에 다시 넣기
# 다시 리스트 오름차순 정렬 후 맨앞 두개 꺼내서 합한 값 모두 결과에 추가해주기
# 시간초과.... => 아예 가장작은수 두개를 꺼내서 교체하고 이런거 해준ㄴ게 따로 있나?
