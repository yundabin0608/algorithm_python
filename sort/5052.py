# 전화번호 목록
# 전화번호 목록이 주어질 경우 목록이 일관성 있는지 없는지 구하는 프로그램
# 일관성있으려면 한 번호가 다른 번호의 접두어인 경우 X
# 입력 : 테스트케이스 개수, 케이스마다 전화번호수 n과 n개의 전화번호 (길이 최대 10)
# 출력 : Yes / No (일관성 유무)
# pypy3로 해야 통과

t = int(input())

for i in range(t):
    
    n=int(input())
    num_list=[]
    for _ in range(n):
        num_list.append(input()) # 문자열로 넣었으므로 인덱스로 사용가능

    num_list.sort() # 앞 문자가 작은번호순으로 정렬됨 => 앞뒤로만 비교하면 됨
 
    flag=True
    for i in range(n-1):
        length = len(num_list[i])
        if num_list[i] == num_list[i+1][:length]:
            flag=False
            break
        
               
    if flag:
        print('YES')
    else:
        print('NO')