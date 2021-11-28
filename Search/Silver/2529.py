# 부등호

# 부등호 기호 앞뒤 서로 다른 한자리 숫자 넣어 모든 관계 만족시킬것
# 부등호 앞뒤에 넣을 수 있는 숫자는 0~9, 선택된 숫자는 모두 다를것
# k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값
# 입력: 2~9인 k (부등호 갯수), 밑의 줄은 k개의 부등호 기호
# 출력: 부등호 만족하는 최대 최소 정수 출력 (앞자리 0도 포함)

k = int(input())
list = input().split() 
max, min= "",""
num = [0]*10


def possible(i, j, sign):
    if sign == '>':
        return i > j
    else:
        return i < j


def solve(depth, s):
    global max, min

    if depth == k + 1:
        if len(min) == 0: # 즉 최소값 없으면, (처음숫자가 최솟값일것이므로)
            min= s
        else:
            max = s
        return

    for i in range(10):
        if num[i]==0: # 아직 사용하지 않은 숫자라면
            if depth == 0 or possible(s[-1], str(i), list[depth - 1]):
                num[i] = True
                solve(depth + 1, s + str(i))
                num[i] = False


solve(0, "")
print(max)
print(min)

# 백트래킹 생각안나서 답지봄
# 새로운 수가 추가될때마다 부등호 조건에 맞는지 확인하는 함수 생성
# 중복없는 0~9를 사용하기 위해 num 배열과 for 반복문을 사용
# 숫자는 0부터 커지므로 처음만들어지는게 최소값 즉 solve의 조건문