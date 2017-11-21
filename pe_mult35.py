def sum(n, k):
	p = (n - 1)//k
	return k * (p + 1) * p/2


n = 1000
val = sum(n, 3) + sum(n, 5) - sum(n, 15)
print(val)