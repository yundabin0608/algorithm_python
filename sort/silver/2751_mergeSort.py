def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:]) 
    merged = []

    i, j = 0, 0
    while i < len(left) and j < len(right): 
        if (left[i] > right[j]):
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1

    if i != len(left):
        merged += left[i:]
    if j != len(right):
        merged += right[j:]
    return merged

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))
    
result = merge_sort(numbers)

for n in result:
	print(n)