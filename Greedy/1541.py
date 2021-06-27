# 잃어버린 괄호
# 양수, +, - 인식에 적당히 괄호 쳐서 식의 값 최소로 만들기
# 식 처음, 끝은 숫자이고 둘 이상의 연산자가 나올 수 없음, 5자리 이상 연속 숫자 없음, 식길이 50 이하

expr = input()
expr2 = expr.split('-')
n = len(expr2)

# -부터 다음 -까지 괄호쳐서 음수만들면 그게 최소 
# 즉 -로 split 후 각각 나눠진애들은 +로 나눠서 sum으로 합 구하기
for i in range(0,n):
    addList = expr2[i].split('+')
    expr2[i] = sum(map(int,addList))

answer = int(expr2[0])
if (n>1):
    for i in range(1, n):
        answer -= int(expr2[i])

print(answer)