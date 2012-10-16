
from numpy import *

file = open("Exp6/contacts.Exp6.dat")
out  = open("infocomICT.txt","w")
ict = zeros((30000,1), dtype=int)
contype = ['down','up']


for line in file:
	l=line.split()
	id1=int(l[0])
	id2=int(l[1])
	stc=int(l[2])
	enc=int(l[3])
	CT = int(l[5]) 
	if id1>98 or id2>98 or  enc <= stc or CT>25000 :
		continue 
	if id1 < 21 or id2 < 21 :
		continue
	if id1 == id2:
		continue
	ict[CT]=ict[CT]+1

t = 0
for line in ict:
	out.write(str(t)+'\t'+str(line[0])+'\n')
	t=t+1



