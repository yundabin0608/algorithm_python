# 연산자 끼워넣기
N=int(input())
numbers=list(map(int, input().split()))
add, sub, mul, div =map(int, input().split())

min_ans=1000000000
max_ans=-100000000

def dfs(now, answer, add, sub, mul, div):
    global max_ans, min_ans
    if now == N-1:
        max_ans=max(answer, max_ans)
        min_ans=min(answer,min_ans)

    else:
        if add:
            dfs(now+1, answer+numbers[now+1], add-1, sub, mul, div)
        if sub:
            dfs(now+1,answer-numbers[now+1], add, sub-1, mul, div)
        if mul:
            dfs(now+1,answer*numbers[now+1], add, sub, mul-1, div)
        if div:
            dfs(now+1,int(answer/numbers[now+1]), add, sub, mul, div-1)

dfs(0, numbers[0], add, sub, mul, div)
print(max_ans)
print(min_ans)

