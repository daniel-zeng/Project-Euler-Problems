def poly(n, type):
	ret = 0
	if type == 3:
		ret = n*(n + 1)/2
	elif type == 5:
		ret = n*(3*n - 1)/2
	elif type == 6:
		ret = n*(2*n -1)
	return int(ret)

maxsearch = 1000000
tri = set(poly(n, 3) for n in range(285, maxsearch))
pent = set(poly(n, 5) for n in range(165, maxsearch))
hexo = set(poly(n, 6) for n in range(143, maxsearch))

res = 0
for i in tri:
	if(i in pent and i in hexo):
		print(i)