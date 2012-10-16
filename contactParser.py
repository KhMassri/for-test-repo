
from numpy import *

file = open("Exp6/contacts.Exp6.dat")
out  = open("infocomS21_78_D_21_78.txt","w")
con = zeros((151000,4), dtype=int)
contype = ['down','up']

index = 0

for line in file:
	l=line.split()
	id1=int(l[0])
	id2=int(l[1])
	stc=int(l[2])
	enc=int(l[3])
	if id1>98 or id2>98 or  enc <= stc :
		continue
	if id1 < 21 or id2 < 21 :
		continue



	con[index][0]=stc
	con[index][1]=id1
	con[index][2]=id2
	con[index][3]=1
	index = index+1
	con[index][0]=enc
	con[index][1]=id1
	con[index][2]=id2
	con[index][3]=0
	index=index+1


con.view('i8,i8,i8,i8').sort(order=['f0'], axis=0)

for line in con:
	out.write(str(line[0])+'\t'+'CONN'+'\t'+str(line[1])+'\t'+str(line[2])+'\t'+contype[line[3]]+'\n')



