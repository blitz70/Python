#   36. Regular expression

'''
Identifiers, sequences
\d    any number
\D    not number
\s    space
\S    not space
\w    any letter
\W    not letter
.     any character, except newline
\b    whitespace around words
\.    a period

Modifiers, characters
{1,3} expect 1-3
+     match 1 or more
?     match 0 or 1
*     match 0 or more
^     match start of string
$     match end of a string
|     matche either/or
[]    range or 'variance'
{x}   expect 'x' times

Whitespace characters
\n    new line
\s    space
\t    tab
\e    escape
\f    form feed
\r    return

Don't forget to use escape
. + * ? $ ^ | \ () [] {}
'''

import re

exampleStr = '''
Jessica is 15 year old, and Daniel is 27 years old.
Edward is 77, and his grandfrather Oscar is 102.
Henry's age isn't known.
'''

ages = re.findall(r'\d{1,3}',exampleStr)
names = re.findall('[A-Z][a-z]*',exampleStr)
print(names)
print(ages)

'''
personDic = {}
count =0
for name in names: #kinda sloppy
    personDic[name]= ages[count]
    count+=1
print(personDic)
'''

personZip = zip(names,ages)
personDict1 = dict(zip(names,ages))
print(personDict1)

personDict2 = {a:b for a,b in zip(names,ages)}
print(personDict2)






