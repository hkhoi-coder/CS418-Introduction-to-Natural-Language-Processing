# Name: Hoang Khoi
# ID = 1351026

import sys
import os
import re
import pprint

# hkhoi@outlook.com|hkhoi&#x40;outlook.com
# hkhoi WHERE outlook DOM edu
# hkhoi at outlook dot com|hkhoi at outlook.com|hkhoiat outlook;com
# ('outlook.com', 'hkhoi')
# w-t-f-i-s-t-h-i-s-s-h-i-t-@-s-h-i-t-.-c-o-m
# ouster (followed by &ldquo;@cs.stanford.edu&rdquo;)|ouster (followed by "@cs.stanford.edu")
# hkhoi at outlook com

email_pattern0 = r'([\w\.]+) ?(@|&#x40;) ?(\w+(\.\w+)+)'
email_pattern1 = r'([\w\.]+) WHERE (\w+) DOM (\w+)'
email_pattern2 = r'\W([a-z0-9]+(( dot |\.|;| dt )\w+)* at \w+(( dot |\.|;| dt )\w+)+)'
email_pattern3 = r'\(\'([\w\.]+)\',\'([\w\.]+)\'\)'
email_pattern4 = r'(\w(-\w|-\.)+-@-\w(-\w)+-.(-\w)+)'
email_pattern5 = r'([\w\.]+) \(followed by ("|&ldquo;)@(\w+(\.\w+)+)'
email_pattern6 = r'(\w+) at ([\w ]+) stanford edu'

# (xxx)xxx-xxxx
# x xxx xxx xxxx
phone_patter0 = r'\b\(?(\d{3})\)? ?-?(\d{3})-(\d{4})'
phone_patter1 = r'\+\d+ ?-?(\d{3}) ?-?(\d{3}) ?-?(\d{4})'

test = r'\(\d{3}\)\d{3}-\d{4}'

""" 
TODO
This function takes in a filename along with the file object (actually
a StringIO object at submission time) and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers

NOTE: ***don't change this interface***, as it will be called directly by
the submit script

NOTE: You shouldn't need to worry about this, but just so you know, the
'f' parameter below will be of type StringIO at submission time. So, make
sure you check the StringIO interface if you do anything really tricky,
though StringIO should support most everything.
"""
def process_file(name, f):
    # note tha([\w\.]+) ?@ ?([\w\.]+)\.(edu|com|net|edu|org|vn)ted to stderr
    # sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))
    res = []
    for line in f:
        email_matches0 = re.findall(email_pattern0,line)
        email_matches1 = re.findall(email_pattern1, line)
        email_matches2 = re.findall(email_pattern2, line)
        email_matches3 = re.findall(email_pattern3, line)
        email_matches4 = re.findall(email_pattern4, line)
        email_matches5 = re.findall(email_pattern5, line)
        email_matches6 = re.findall(email_pattern6, line)

        phone_matches0 = re.findall(phone_patter0, line)
        phone_matches1 = re.findall(phone_patter1, line)

        test_match = re.findall(test, line)

        # Pattern 0:
        for m in email_matches0:
            email = '%s@%s' % (m[0], m[2])
            res.append((name, 'e', email))
        # Pattern 1:
        for m in email_matches1:
            email = '%s@%s.%s' % m
            res.append((name, 'e', email))
        # Pattern 2:
        for m in email_matches2:
            email = m[0].replace('at', '@').replace('dot', '.').replace('dt','.').replace(';', '.').replace(' ', '')
            res.append((name, 'e', email))
        # Pattern 3:
        for m in email_matches3:
            email = '%s@%s' %m[1::-1]
            res.append((name, 'e', email))
        # Pattern 4:
        for m in email_matches4:
            email = m[0].replace('-', '')
            res.append((name, 'e', email))
        # Pattern 5:
        for m in email_matches5:
            email = '%s@%s' %(m[0], m[2])
            res.append((name, 'e', email))
        # Pattern 6:
        for m in email_matches6:
            email = '%s@%s.stanford.edu' %m[0:2]
            res.append((name, 'e', email))
        for m in phone_matches0:
            phone = '%s-%s-%s' % m
            res.append((name, 'p', phone))
        for m in phone_matches1:
            phone = '%s-%s-%s' % m
            res.append((name, 'p', phone))

        # Testing:
        # for m in test_match:
        #     print 'DEBUG:', m
    return res
"""
You should not need to edit this function, nor should you alter
its interface as it will be called directly by the submit script
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a tsv file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print 'True Positives (%d): ' % len(tp)
    pp.pprint(tp)
    print 'False Positives (%d): ' % len(fp)
    pp.pprint(fp)
    print 'False Negatives (%d): ' % len(fn)
    pp.pprint(fn)
    print 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn))

"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""
def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print 'usage:\tSpamLord.py <data_dir> <gold_file>'
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])
