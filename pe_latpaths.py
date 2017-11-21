size = 21
arr = [([1] * size) for i in range(size)]

for r in range(1, size):
	for c in range(1, size):
		arr[r][c] = arr[r - 1][c] + arr[r][c - 1]
print(arr)
print(arr[-1][-1])