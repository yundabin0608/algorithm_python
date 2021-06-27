# 집합
# 빈 공집합 S 
# add x : S에 x추가 있으면 무시, remove x : S에서 x제거 없으면 무시
# check x : S에 x 있>1 없>0 출력, toggle x : S에 x가 있으면 제거, 없으면 무시
# all : S를 1,2,...,20으로 바꾸기, empty : 공집합으로 만들기

import sys
input = lambda : sys.stdin.readline().strip() # 이거 추가해주니까 됨

M=int(input())
S=[]

for i in range(M):
    In = input().split()
   

    if (In[0]=='all'):
        S.clear()
        S = [i for i in range(1,21)]
        continue
    elif(In[0]=='empty'):
        S.clear()
        continue
    
    num = int(In[1])
        
    if (In[0]=='add'):
        if num not in S :
            S.append(num)
    elif (In[0]=='remove'):
        if num in S :
            S.remove(num)
    elif (In[0]=='check'):
        if num in S :
            print('1')
        else :
            print('0')
    elif (In[0]=='toggle'):
        if num in S :
            S.remove(num)
        else :
             S.append(num)
    


## tlqkf 왜 시간초과

M=int(input())
S=[]

for i in range(M):
    In = input().split()
   
    if (len(In)==1):
        if (In[0]=='all'):
            S.clear()
            S = [i for i in range(1,21)]
        else :
            S.clear()
    else :
        num = int(In[1])
        
        if (In[0]=='add'):
            if num not in S :
                S.append(num)
        elif (In[0]=='remove'):
            if num in S :
                S.remove(num)
        elif (In[0]=='check'):
            if num in S :
                print('1')
            else :
                print('0')
        elif (In[0]=='toggle'):
            if num in S :
                S.remove(num)
            else :
                S.append(num)




