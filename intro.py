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
'''

sentence = 'Start a sentence and then bring it to an end'


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
word_pattern = re.compile(r'\w+@\w+\.\w+\b')
 
words = word_pattern.finditer(file)

for word in words: 
    print(word)

pattern = re.compile(r'\d[\d\.-]*\d')
matches = pattern.finditer(text_to_search)


# \s - Whitespace (space, tab, \n), \S - Not whitespace, space, tab, \n 
# \d - (0 - 9), \D not a digit 
# \w Word character, \W not  word character (\n, )
# \b - Word boundary, \B not a word boundary 
#^ Beginning of a string, $end of a string 
# [] Matches characters in brackets 
# [^ ] Matches characters not in brackets 
for match in matches:
    print(match)

print(text_to_search[slice(1, 4)])