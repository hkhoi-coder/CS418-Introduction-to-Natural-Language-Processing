import sys

def med(str0, str1):
	len0 = len(str0)
	len1 = len(str1)
	
	result = [[0 for x in range(len1 + 1)] for x in range(len0 + 1)]
	# Down, Diag, Right, DiagKeep
	trace = [[[False, False, False, False] for x in range(len1 + 1)] for x in range(len0 + 1)]
	action = ['I', 'S', 'D', 'K']
	
	for i in range(0, len0 + 1):
		for j in range(0, len1 + 1):
			if i == 0:
				result[i][j] = j
				trace[i][j][2] = True
			elif j == 0:
				result[i][j] = i
				trace[i][j][0] = True
			else:
				choice0 = result[i - 1][j] + 1
				choice1 = result[i][j - 1] + 1
				choice2 = result[i - 1][j - 1]
				
				sub_flag = False
				
				if str0[i - 1] != str1[j - 1]:
					choice2 += 2
					sub_flag = True
				
				min_value = min(choice0, min(choice1, choice2))
				
				if min_value == choice0:
					trace[i][j][0] = True
				if min_value == choice1:
					trace[i][j][2] = True
				if min_value == choice2:
					if sub_flag:
						trace[i][j][1] = True
					else:
						trace[i][j][3] = True
				
				result[i][j] = min_value		

	# Traceback
	i = len0
	j = len1
	
	stack_trace = []
	
	while not (i == 0 and j == 0):
		
		cur_trace = trace[i][j]
		
		if cur_trace[0]: down = result[i - 1][j] 
		else: down = sys.maxint
		if cur_trace[1] or cur_trace[3]: diag = result[i - 1][j - 1]
		else: diag = sys.maxint
		if cur_trace[2]: right = result[i][j - 1]
		else:right = sys.maxint
		
		if diag <= right and diag <= down:
			if cur_trace[1]:
				stack_trace.append(1)
			else:
				stack_trace.append(3)
			i -= 1
			j -= 1
		elif right <= down and right <= diag:
			stack_trace.append(2)
			j -= 1
		elif down <= right and down <= diag:
			stack_trace.append(0)
			i -= 1
	print 'MED = ', result[len0][len1]
	print 'Alignment instructions: ',
	for i in stack_trace:
		print action[i],
		
print 'NOTE: This is the instruction to transform str0 into str1'
print 'NOTE: the instruction is the TRACE STACK, so read it backward!'
print 'NOTE: K: Keep, D: Delete, I: Insert, S: Subtitute'
str0 = raw_input('str0 = ')
str1 = raw_input('str1 = ')
med(str0, str1)
