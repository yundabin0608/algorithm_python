#감시피하기 -- combination을 이용한 구현
from itertools import combinations

N= int(input())
student_index=[]
teacher_index=[]
empty_index=[]


# 주어진 정보를 담고 학생과 선생 좌표를 리스트에 담음
matrix=[]
for i in range(N):
   matrix.append(list(input().split()))
   for j in range(N):
       if matrix[i][j] == 'S':
           student_index.append([i,j])
       if matrix[i][j] == 'T':
           teacher_index.append([i,j])
       if matrix[i][j] =='X':
           empty_index.append([i,j])


direction = [[-1,0],[1,0],[0,-1],[0,1]]

# 남는 빈칸들 중에 3개를 무작위로 뽑아서 벽을 세움
for wall in combinations(empty_index,3):
    for x,y in wall:
        matrix[x][y]='O'
    
    flg =False
    for t in teacher_index:
        for i in range(4):
            x,y=t
            while 0<=x and x<=N-1 and 0<=y and y<=N-1 and matrix[x][y] != 'O':
                if matrix[x][y] == 'S':
                    flg=True 
                    break
                x+=direction[i][0]
                y+=direction[i][1]
            if flg:
                break
        if flg:
            break
    if not flg:
        print('YES')
        exit()

    for x,y in wall:
        matrix[x][y]='X'

print('No')