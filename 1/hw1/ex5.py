def med(str0, str1):
	len0 = len(str0)
	len1 = len(str1)
	
	result = [[0 for x in range(len1 + 1)] for x in range(len0 + 1)] 
	for i in range(0, len0 + 1):
		for j in range(0, len1 + 1):
			if i == 0:
				result[i][j] = j
			elif j == 0:
				result[i][j] = i
			else:
				choice0 = result[i - 1][j] + 1
				choice1 = result[i][j - 1] + 1
				choice2 = result[i - 1][j - 1]
				if str0[i - 1] != str1[j - 1]:
					choice2 += 2	
					
				result[i][j] = min(choice0, min(choice1, choice2))
				
	# Print out the matrix for testing:
#	for i in range(0, len0 + 1):
#		for j in range(0, len1 + 1):			
#			print result[i][j],' ',
#		print			

	return result[len0][len1]
	
str0 = raw_input('Input string0: ')
str1 = raw_input('Input string1: ')
print 'MED = ', med(str0, str1)
