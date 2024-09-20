#program to remove duplicates from string


string="this this this this"

s=set(string.split()[::])
#for i in s:


print(s)