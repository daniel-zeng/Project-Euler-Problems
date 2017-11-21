#	 	   0    1   2   3  4   5  6  7
coins = [200, 100, 50, 20, 10, 5, 2, 1]
coinsRev = list(reversed(coins))
dp = {}
iteration = 0

def solveBase(n):
	total = solveBrute(n, 0)
	return total

def bottomUpDP(n):
	
	dp[0] = 1
	for idx in range(1, len(coinsRev)):
		ways = 0
		for idx2 in range(0, idx):
			ways += dp[idx2]
		dp[idx] = ways
	print(dp)


def solveBrute(n, curr):
	global iteration

	if(n == 0):
		return 1
	if(curr == 7):
		return 1
	iteration += 1

	coin = coins[curr]
	ret = 0
	numC = 0
	while 1:
		if(numC * coin > n):
			break
		ret += solveBrute(n - numC * coin, curr + 1)
		numC += 1
	return ret


cns = 200
print(solveBase(cns), iteration)
bottomUpDP(200)