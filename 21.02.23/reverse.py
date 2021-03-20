# 숫자인 문자열 리스트에 한글자식 int로 변형해서 담기
s = list(map(int,input()))
count=0

num1=0
num0=0
result=0

# 1과 0의 갯수 세어 판단 적은것 뒤집는게 유리, 둘중 하나라도 없으면 -1 반환
def judge(list) :    

    for i in list:
        num1+1 if (s[i]==1) else num0+1
        
    if (num1 <= num0):
        result + 1 

    if(num1 == 0 or num0 ==0):
        result - 1
    

def rev(list, res):

    if (res==0):
        for i in list:
            if(list[i]==0):
                list[i]=1
    else:
        for i in list:
            if(list[i]==1):
                list[i]=0

    result=0


# 뒤집을 숫자 판단후 뒤집을거 없으면 while 나가고 있으면 rev함수로 뒤집고 count++
while True:

    judge(s)
    
    if (result<0): break

    rev(s, result)
    count+=1

print(count)