judge=list(map(int,input()))

half = int(len(judge) / 2)
left=0
right=0

for i in range(0,half):
    left+=judge[i]

for i in range(half, half*2):
    right+=judge[i]

print("LUCKY") if (left == right) else print("READY")