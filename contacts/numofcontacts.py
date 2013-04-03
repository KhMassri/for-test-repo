from numpy import *
import scipy.io as sio
N = 80
D = '1'
CCP = zeros((30,N))
# nodes Ids start from 21 to 98 S = 0 and D = 1
#f=open('infocomS0_11_15_D1_2_13.txt')
'''
To read 30 contact files and average them then save it as matlab data.
'''
for i in range(30):
    curProb = zeros(N)
    f=open('./tvc_contacts/tvc'+str(i)+'.txt')
    for line in f.readlines():
      con = line.split()
      if (con[2]==D or con[3]==D) and con[4]=='up':
        if con[2]== D:
          index=int(con[3]) #-20
        else:
          index=int(con[2]) #-20
        if index < 0:#1
          print 'error'
        curProb[index]=curProb[index]+1
        
    curProb = curProb/sum(curProb)
    curProb = sort(curProb)
    curProb = curProb[::-1]
    
    for j in range(1,len(curProb)):
      curProb[j]=sum(curProb[j-1:j+1])
      
    CCP[i] = curProb
    
avgCCP = [average(CCP[:,n]) for n in range(N)]
sio.savemat('tvcAvgCCP.mat', mdict={'tvcCCP': avgCCP})


import matplotlib.pyplot as plot
plot.title(r'x * 2 and x ** 2')
plot.plot(avgCCP, label=r'$prob$', color='red')
plot.legend(loc='upper right')
plot.grid()
plot.show()
	
