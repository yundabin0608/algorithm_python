# 전화번호 목록
# 전화번호 목록이 주어질 경우 목록이 일관성 있는지 없는지 구하는 프로그램
# 일관성있으려면 한 번호가 다른 번호의 접두어인 경우 X
# 입력 : 테스트케이스 개수, 케이스마다 전화번호수 n과 n개의 전화번호 (길이 최대 10)
# 출력 : Yes / No (일관성 유무)

t = int(input())

for i in range(t):
    
    n=int(input())
    num_list=[]
    for _ in range(n):
        num_list.append(input()) # 문자열로 넣었으므로 인덱스로 사용가능

    flag='YES'
    for num in num_list:
        
        for i in range(len(num_list)):
            if num in num_list[i][0:len(num)] :
                flag='NO'
                break
    
    print(flag)


    