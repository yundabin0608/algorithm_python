# LCS 최장 공통 부분 수열
# 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾기
# 1,2줄은 두 문자열 (대문자 최대 1000자)
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력
# 연속적이지 않은 부분 문자열

s1=list(input())
s2=list(input())
result=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]

len_s1=len(s1)
len_s2=len(s2)
 
# 점화식 수행
for i in range(1,len_s1+1):
    for j in range(1,len_s2+1):
        if s1[i-1]==s2[j-1]:
            result[i][j]=result[i-1][j-1]+1
        else:
            result[i][j]=max(result[i-1][j],result[i][j-1])
 
print(result[len_s1][len_s2])