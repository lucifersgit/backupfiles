import re

message = 'Call me at 415-555-1234 tomorrow, or at 415-555-1321'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())
