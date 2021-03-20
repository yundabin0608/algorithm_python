N=int(input())

stars=[[' ' for _ in range(N)] for _ in range(N)]


def fill(size, x, y):
    if size==1:
        stars[x][y]="*"
    else:
        nextSize=size//3
        for dy in range(3):
            for dx in range(3):
                if dy !=1 or dx!=1:
                    fill(nextSize, x+dx*nextSize, y+dy*nextSize)

fill(N,0,0)
for k in range(N):
    print(''.join(stars[k]))