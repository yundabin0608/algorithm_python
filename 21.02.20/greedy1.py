# m번 더해 가장큰수. k번 초과하여 더할 수 없음
N, M, K = map(int, input().split())    
nlist = list(map(int, input().split()))
sum = 0
# 숫자 리스트를 만든뒤 이를 크기별로 정렬하고 하나씩 쓰도록할것이다.
nlist.sort(reverse=True)


repeat = M//(K+1)
bundle = (nlist[0] * K) + nlist[1]
remainder = M%(K+1)

if remainder == 0:
    tail = 0
else:
    tail = nlist[0]*remainder

sum = (bundle * repeat) + tail
print(sum)