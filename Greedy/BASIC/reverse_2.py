s = list(map(int, input()))
count=0

# 범위 그냥 리스트 넣으려다가 그러면 if문 범위가 틀어졋 i~i+1 i-1~i 모두 안대
for i in range(len(s)-1):
    if(s[i] != s[i+1]):
        count+=1

print(count//2) if(count%2==0) else print((count+1)//2)
    
