# 1. 국영수
# 조건에 맞춰 학생 정렬하기

N = int(input())

# 학생들에 관한 정보 리스트 [이름, 국, 영, 수]
students=[]
for i in range(N):
    students.append(input().split())
    #!!!! 시간초과 오류
#시간초과가 안되는 입력받는 형식을 확실히 해야겠음

# 국어 점수 큰놈 - 영어점수 작은놈 - 수학점수 큰놈 (순으로 맨앞)
for i in range(N):
    min_index=i
    for j in range(i+1,N):
        if int(students[min_index][1])<int(students[j][1]):
            min_index=j
        elif int(students[min_index][1]) == int(students[j][1]):
            if int(students[min_index][2]) > int(students[j][2]):
                min_index=j
            elif int(students[min_index][2]) == int(students[j][2]):
                if int(students[min_index][3]) < int(students[j][3]):
                    min_index=j
                elif int(students[min_index][3]) == int(students[j][3]):
                    if students[min_index][0] > students[j][0]:
                        min_index=j

    # 스와프. 선택정렬 이용
    students[i],students[min_index]=students[min_index],students[i]

for i in range(N):
    print(students[i][0])




# 2. 안테나
# 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 안테나 한개 설치 (위치 선택해줌)
# 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능

# 집의 개수
N = int(input())

# 집들의 위치
h_location = list(map(int, input().split()))

result = [] * N

for i in h_location:
    total=0
    for j in h_location:
        total+=abs(j-i)
        # 절대값 함수 abs() 내장함수임
    result.append([total, i])

result.sort(key=lambda result: (result[0], result[1]))
print(result[0][1])

# 3.카드 정렬하기
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
# oo heapq 이용해야함 이거 개념 정리하자..