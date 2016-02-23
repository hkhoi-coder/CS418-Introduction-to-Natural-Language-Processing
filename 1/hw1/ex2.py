# Name/ID = Hoang Khoi/1351026

import string, re, random

SAD_PATTERN = r'.*\b(depressed|sad|not happy)\b.*'
ALL_PATTERN = r'.*\b(all|every)\b.*'
ALWAYS_PATTERN = r'.*\b(always|often)\b.*'
FINE_PATTERN = r'.*\b(good|nice|happy|ok|fine)\b.*'

NO_IDEAS = (
	'I have no ideas what you are talking about',
	'I am a bot, not a human!', 
	'Say something easier to understand!')
RES_FINE = (
	'Nice to hear that, now, gimme a good grade please!',
	'OK, good to know that',
	'Sweet, now do something to damage your healthy life!'
)
RES_ALWAYS = (
	'What makes you say that?',
	r'You said always... Really?',
	'For real?'
)
RES_ALL = (
	'You are confident? aren\'t you?'
	'Prove what you say!'
	'I don\'t think so'
)
RES_SAD = (
	'Yeah, serve you right',
	'Awww! What \'s up?',
	'Huehuehuehuehue!!!'
)

user_str = ''	# user input

def is_sad():
	return re.match(SAD_PATTERN, user_str)
def is_all():
	return re.match(ALL_PATTERN, user_str)
def is_always():
	return re.match(ALWAYS_PATTERN, user_str)
def is_fine():
	return re.match(FINE_PATTERN, user_str)
print 'Welcome to ELIZA talk show! Press Ctrl-C (Linux) to exit :)'

exit_flag = False
while not exit_flag:
	user_str = raw_input('>user: ')
	user_str = user_str.lower()
	
	if is_sad():
		print '>ELIZA: ',random.choice(RES_SAD)
	elif is_all():
		print '>ELIZA: ',random.choice(RES_ALL)
	elif is_always():
		print '>ELIZA: ',random.choice(RES_ALWAYS)
	elif is_fine():
		print '>ELIZA: ',random.choice(RES_FINE)
	else:
		print '>ELIZA: ',random.choice(NO_IDEAS)
		
		
