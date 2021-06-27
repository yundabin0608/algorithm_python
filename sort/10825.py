# 국영수 문제 - 점수순으로 학생 정렬

N = int(input())

# 학생들에 관한 정보 리스트 [이름, 국, 영, 수]
students=[]
for i in range(N):
    name, kor, eng, math = input().split()
    students.append([str(name), kor, eng, math])  
    
students.sort(key= lambda students: (-int(students[1]), int(students[2]), -int(students[3]), students[0]))

for i in range(N):
    print(students[i][0])