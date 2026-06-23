import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat
pat
dat
sat

'''

sentence = 'Start a sentence and then bring it to an end'

# \s - Whitespace (space, tab, \n), \S - Not whitespace, space, tab, \n 
# \d - (0 - 9), \D not a digit 
# \w Word character, \W not  word character (\n, )
# \b - Word boundary, \B not a word boundary 
#^ Beginning of a string, $end of a string 
# [] Matches characters in brackets 
# [^ ] Matches characters not in brackets 
# for match in matches:
# quantifiers : * - 0 or more; + 1 or more; ? 0 or None, {3} exactly 3 or specified Number; {3, 4} a range of 3 to 4 elements or a range {minimum, maximum}


#predominantly we are going to be using raw strings 

# pattern = re.compile(r'[a-z A-Z 0-9]+\.com')
# pattern = re.compile(r'[\w]+\.\s')

with open('data.txt', 'r') as f: 
    file = f.read()

#=================================
#phone numbers 
#=================================


# word_pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
 
# words = word_pattern.finditer(file)

# for word in words: 
#     print(word)


#=================================
# emails 
#=================================
# word_pattern = re.compile(r'\w+@\w+\.\w+\b')
 
# words = word_pattern.finditer(file)

# for word in words: 
#     print(word)

#=================================
# Addresses 
#=================================
# word_pattern = re.compile(r'\d+ \w+ \w+., \w+ \w+ \d+')
 
# words = word_pattern.finditer(file)

# for word in words: 
#     print(word)

#=================================
# Names (that needs cleanup to eliminate the last character, and also sorting for 3 names)
#=================================
# word_pattern = re.compile(r'\w+ \w+\n\d')
#word_pattern = re.compile(r'[a-zA-Z]* [a-zA-Z]*\n\d')
 
# words = word_pattern.finditer(file)

# for word in words: 
#     print(word)

#=================================
# Names with cleaned up output 
#=================================

# word_pattern = re.compile(r'[a-zA-Z]* [a-zA-Z]*\n\d')
 
# words = word_pattern.finditer(file)

# for word in words: 
#     to_print = word.group(0).split('\n')[0]
#     print(to_print)



# word_pattern = re.compile(r'[a-zA-Z]a[a-zA-Z]\b')
 
# words = word_pattern.finditer(text_to_search)

# for word in words: 
#     print(word)

#=================================
#urls 
#=================================

urls = '''
https://www.google.com
https://coreyms.com 
http://youtube.com
https://www.nasa.gov
'''

#word_pattern = re.compile(r'[a-zA-z]*\.?[a-zA-Z0-9]+\.[a-zA-Z]+')

word_pattern = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+)\.(com|gov)')
 
# words = word_pattern.finditer(urls)

# for word in words: 
#     print(word.group(0))
#     print(word.group(1))
#     print(word.group(2))

words = word_pattern.findall(urls)

for word in words: 
    print(word)


# subs = word_pattern.sub(r'\2', urls)

# print(subs)

# pattern = re.compile(r'\d[\d\.-]*\d')
# matches = pattern.finditer(text_to_search)



#     print(match)

# print(text_to_search[slice(1, 4)])