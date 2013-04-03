from numpy import *
import scipy.io as sio
N = 80 #79
D = '1'
count = zeros(N)
# nodes Ids start from 21 to 98 S = 0 and D = 1
f=open('tvc.txt')
for line in f.readlines():
  con = line.split()
  if (con[2]==D or con[3]==D) and con[4]=='up':
    if con[2]== D:
      index=int(con[3]) #-20
    else:
      index=int(con[2]) #-20
    if index < 0:#1
      print 'error'
    count[index]=count[index]+1
    
count = count/sum(count)
count = sort(count)
count = count[::-1]

for i in range(1,len(count)):
  count[i]=sum(count[i-1:i+1])

sio.savemat('tvcdata.mat', mdict={'tvc': count})


import matplotlib.pyplot as plot
plot.title(r'x * 2 and x ** 2')
plot.plot(count, label=r'$prob$', color='red')
plot.legend(loc='upper right')
plot.grid()
plot.show()
	
	
