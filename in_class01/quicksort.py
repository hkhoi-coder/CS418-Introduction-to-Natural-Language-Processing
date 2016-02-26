def quicksort(a):
	__partition(a, 0, len(a) - 1)

def __partition(a, left, right):
	print 'DATA:', a
	print 'BEGIN:',left,right
	if left >= right:
		print 'END:',left,right
		print
		return

	i = left + 1
	j = right
	pivot = a[left]

	isOK = False

	while not isOK:
		while i < right and a[i] <= pivot:
			i += 1
		while j > left and a[j] > pivot:
			j -= 1
		print 'i:',i,'j:',j
		if i < j:
			print 'SWAP:',i, j, a[i],a[j]
			a[i], a[j] = a[j], a[i]
			i += 1
			j -= 1
			print 'DATA:', a
		else:
			print 'SWAP:',left, j, a[left],a[j]
			a[j], a[left] = a[left], a[j]
			isOK = True
			print 'DATA:', a

	print
	__partition(a, left, j - 1)
	__partition(a, j + 1, right)
	print 'END:',left,right
	print

a = [76,194,457,146,75,413,61,751,974,67,168,716,139,87,597,814]
quicksort(a)
print a