import re
regex = re.compile(r"'(.*?)\'")
result = regex.search("'hei' + 'nei'")
print(result)