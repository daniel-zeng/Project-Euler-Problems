dp = {}

def fib(n):
	if n < 4:
		return n
	if n in dp:
		return dp[n]
	ret = fib(n - 1) + fib(n - 2)
	dp[n] = ret
	return ret

counter = 1
sum = 0
while 1:
	val = fib(counter)
	print(val, counter)
	if val < 4000000 and val % 2 == 0:
		sum += val

	elif val >= 4000000:
		break
	counter += 1

print("sum", sum)