fin = open('pe_13.in')
summ = 0
for line in fin:
	summ += int(line)

print (str(summ)[0:10])