# 가로수
# 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하기
# 단, 추가되는 나무는 기존의 나무들 사이에만 심을 수 있다.
# 입력 : N - 이미 심어진 가로수 개수, 둘째줄부터 가로수 위치
# 출력 : 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수

# 최대공약수를 구해주는 gcd 함수가 있다..! from math import gcd 하고 쓰면됨

N=int(input())
trees = []
gap = []
for i in range(N):
    trees.append(int(input()))
    if (i!=0) : gap.append(trees[i]-trees[i-1])

minGap = min(gap)
for k in range(N-1):
    temp = gap[k]
    if (temp%minGap!=0):
        # 최소값으로 나눠떨어지지 않으면 최대공약수로 변경
        for i in range(min(temp,minGap),0,-1):
            if(temp%i==0 and minGap%i==0): 
                minGap = i
                break
# 최대공약수로 숫자사이 gap들 나눈 몫-1 을 모두 더하면 심을 나무 갯수
answer=0
for i in range(N-1):
    div = gap[i]//minGap
    answer=answer+(div-1)
print(answer)


# 풀이 ======================
# 1 3 7 13
#  2 4 6    (간격)  6/2=3  ->0 
# 2 6 12 18
#  4 6  6   (간격) 6/4 안돼면 6과4의 최대공약수 2