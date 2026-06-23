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
pattern = re.compile(r'[\w]+\.\s')

matches = pattern.finditer(text_to_search)


# \s - Whitespace (space, tab, \n), \S - Not whitespace, space, tab, \n 
# \d - (0 - 9), \D not a digit 
# \w Word character, \W not  word character (\n, )
for match in matches:
    print(match)

print(text_to_search[slice(1, 4)])