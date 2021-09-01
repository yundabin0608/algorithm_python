# 모양 정돈
# 여러 개 ○ □ △ 들이 일렬로 나열 임의의 위치의 두 모양을 서로 맞바꾸는 작업을 반복 => 같은 모양끼리 연속하도록 정돈
# 단, 정돈된 모양의 순서는 상관없다.

# 입력 - 1 : 모양의 전체 개수 N (3~100,000 사이 ) 2 : 나열된 모양들을 나타내는 N개의 정수( 1:△ 2:□ 3:○ ), 각 모양은 최소 한번 이상 나타남
# 출력 - 같은 모양들끼리 연속하도록 정돈하기 위해 필요한 맞바꾸기의 최소 횟수

# 세모, 네모, 동그라미 경우가 6가지니까 6가지별로 집합이랑 원래 입력받은 집합 비교한 후에 그중에 차이가 가장 적게 나는 집합의 원래집합과의 차이나는 원소 개수 구해서 그거 +1 해서 2로 나눈 몫이 답이라고 생각함
n=int(input())
shape=list(input().split())

triangle=shape.count('1')
rectangle=shape.count('2')
circle=shape.count('3')

combination=[['1','2','3',triangle,rectangle,circle],['1','3','2',triangle,circle,rectangle],['2','1','3',rectangle,triangle,circle],['2','3','1',rectangle,circle,triangle],['3','1','2',circle,triangle,rectangle],['3','2','1',circle, rectangle,triangle]]

min_diff=100000
for i in range(6):
    count=0
    first,second,third = combination[i][0],combination[i][1],combination[i][2]
    firstNum=combination[i][3]
    secondNum=firstNum+combination[i][4]
    thirdNum=secondNum+combination[i][5]
    for s in range(n):
        if s<firstNum:
            if shape[s]!=first:
                count+=1
        elif s<secondNum:
            if shape[s]!=second:
                count+=1
        else:
            if shape[s]!=third:
                count+=1

    min_diff=min(min_diff,count)

print((min_diff+1)//2)