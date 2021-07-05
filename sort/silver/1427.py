# 소트인사이드
# 배열 내림차순 정렬
# sort이용 숫자배열 => 문자로 받고 그거를 리스트로 쪼개서 배열로 넣어야됨
# [int(input())] 하면 [1234] NO!! => [1,2,3,4]로 만드는게 관건

n=input()
N=[]
N=list(map(int, n))
print(n, N)

N.sort(reverse=True)

for n in N:
    print(n, end='')





