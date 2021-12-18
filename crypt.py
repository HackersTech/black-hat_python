print('__example__\n')
print(""" for i in rangee(5):\\n\\tprint(i)\nprint('')""")
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

n=exec("new=''\nfor k in a:\n\tp=ord(k)\n\tne=chr(p//300)\n\tnew+=ne\nexec(new)")
j.write(f"{n}")
import os
print('\033[31m operation is successfull',ou,'file is saved in ',os.system('pwd'))

# exec(new)
# for j in a:
#     p=chr(j//2)
#     new+=p
# exec(new)
