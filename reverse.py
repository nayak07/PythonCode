string1='Cisco'

print string1[::-1]

newstring="".join(reversed(string1))
print newstring

revstring=''
for i in range(1,len(string1)+1):
    revstring+=string1[len(string1)-i]
print revstring
