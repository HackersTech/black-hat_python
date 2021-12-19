
e=input("""enter file name->>""")
f=open(e,'r')
kiss=f"""{f.read()}"""
a=[]
new=''
var=[]
for m in kiss:
    kiss=ord(m)
    print(kiss)
    var.append(kiss*300)
print(var)
for i in var:
    a.append(chr(i))
print(a)



ou=input('enter output file name ')

m=open(ou,'w')
m.write('a=')
m.write(f"{a}")

m.close()

j=open(ou,'a')
j.write('\n')
hackrz="""
new=''
for k in a:
    p=ord(k)
    ne=chr(p//300)
    new+=ne
exec(new)"""

j.write(hackrz)
import os
print('\033[31m operation is successfull',ou,'file is saved in ',os.getcwd())

# exec(new)
# for j in a:
#     p=chr(j//2)
#     new+=p
# exec(new)
