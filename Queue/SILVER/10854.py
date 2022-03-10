# 큐
from sys import stdin

N = int(stdin.readline())
queue = []

for i in range(N) :
    text = stdin.readline().split()
 
    if text[0] == 'push' : 
        queue.append(text[1])

    elif text[0] == 'pop' : 
        if queue : print(queue.pop(0))
        else : print(-1)

    elif text[0] == 'size' : print(len(queue))

    elif text[0] == 'empty' :
        if len(queue) == 0 : print(1)
        else : print(0)
            
    elif text[0] == 'front' :
        if len(queue) == 0 : print(-1)
        else : print(queue[0])
    
    elif text[0] == 'back' :
        if len(queue) == 0 : print(-1)
        else : print(queue[-1])