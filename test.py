import re
n  = 2222222222
# match 3 digits or 1-3 digits at the end
ls = re.findall(r"(\d{4}|\d{1,3}$)", str(n))
print(ls[0])
