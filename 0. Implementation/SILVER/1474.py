# 소수 & 펠린드롬

# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 함
# 어떤 수 N 이 있을때, 이보다 크거나 같고 소수이며 팰린드롬인 수들 중 최소 출력

import sys
import math
input = sys.stdin.readline

N = int(input())

def isPalindrome(x):
    string = str(x)
    if string == string[::-1]: return True
    else: return False

def isPrime(x):
    if x==1: return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i == 0: return False
    return True

num = N
while(1):
    if isPalindrome(num) and isPrime(num):
        print(num)
        break
    else : 
        num+=1