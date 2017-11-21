def doRowOld(row, pos, sum):
	sum += tree[row][pos]
	print(tree[row][pos])
	if(row == len(tree) - 1):
		return sum
	if(tree[row + 1][pos] > tree[row + 1][pos + 1]):
		return doRow(row + 1, pos, sum)
	elif tree[row + 1][pos] == tree[row + 1][pos + 1]:
		print("wat")
	else:
		return doRow(row + 1, pos + 1, sum)

#minimax style solution
def doRowNew(row):
	if(row != -1):
		for c in range(len(treeUse[row])):
			treeUse[row][c] += max(treeUse[row + 1][c], treeUse[row + 1][c + 1])
		doRowNew(row - 1)


tree = []

fin = open('maxpathsumii')
for line in fin:
	row = [int(i) for i in line.split()]
	tree.append(row)

treeUse = tree.copy()

doRowNew(len(treeUse) - 2)

print("res", treeUse[0][0])