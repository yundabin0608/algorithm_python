N=int(input())

def answer(N):
    count=1
    if count==N+1:
        return 0
    elif count==N:
        return 1
    else:
        count+=1
        return answer(N-1)+answer(N-2)   

print(answer(N))

#def f(num):
#  if num<=1:
#     return num
#  return f(num-1)+f(num2-2)