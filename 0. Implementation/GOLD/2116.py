# 주사위 쌓기

# 주사위는 모두 정육면체이며 1~6까지 적혀있지만 마주보는 면끼리 합이 7은 아님
# 주사위쌓기는 1부터 순서로 쌓는데 붙어있는 두 주사위에서 아래 주사위 윗면과 위 주사위 아랫면 숫자 같을것
# 이렇게 쌓아두면 긴 사각기둥이 되고 이때 4개의 긴 옆면이 존재하고 이중 한면의 숫자합이 최대가 되게할것
# 한 옆면의 숫자 합의 최댓값을 구할것

import sys
input = sys.stdin.readline

N = int(input())
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))

def dice_max(dices, bott):
    for i in range(6):
        if dices[i] == bott: break
    if i==0: return(dices[5], max(dices[1],dices[2],dices[3],dices[4]))
    elif i==1: return(dices[3], max(dices[0],dices[2],dices[4],dices[5]))
    elif i==2: return(dices[4], max(dices[0],dices[1],dices[3],dices[5]))
    elif i==3: return(dices[1], max(dices[0],dices[2],dices[4],dices[5]))
    elif i==4: return(dices[2], max(dices[0],dices[1],dices[3],dices[5]))
    elif i==5: return(dices[0], max(dices[1],dices[2],dices[3],dices[4]))
    # 주사위는 A,F & B,D & C,E 쌍이므로 맨 아랫면과 옆 4가지면의 최댓값 찾아서 반환

answer= 0
for i in range(1,7):
    
    sum, bottom = 0, i
    for d in range(N):
        bottom, maxD = dice_max(dice[d], bottom)
        sum += maxD
    answer = max(answer, sum)
print(answer)
    
# 위아랫면 붙이고 나문 4가지 숫자의 최대합을 구하면됨
# 1번 주사위의 경우에 따른 총 6가지 경우 존재