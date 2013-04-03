
'''
written by Khalil Massri
'''
from pymobility.models.mobility import tvc
from pymobility.models.contact import mobility_contact

'''
logging all connections up/down at time t 
'''
#out = open('rwp.txt','w')


def print_con(time,cons,stat):
	for peers in cons: 
	  out.write(str(time)+'\tCONN\t'+str(peers[0])+'\t'+str(peers[1])+'\t'+str(stat)+'\n')
	

'''
configureing the mobility model then convert it into contacts
'''

for i in range(30):
		
	out = open('./tvc_contacts/tvc'+str(i)+'.txt','w')
	
	tvcm = tvc([20,20,20,20],(400,200),velocity=(0.8, 1.8), aggregation=[.5,0.0], epoch=[100,100])
	#rwpm = random_waypoint(nr_nodes = 80, dimensions=(400, 200), velocity=(0.8, 1.8), wt_max=100)
	tvcc=mobility_contact(tvcm,contact_range=20)
	#rwpc=mobility_contact(rwpm,contact_range=20)
	
	t=0
	curcon = next(tvcc)
	print_con(t,curcon,'up')
	t=t+1
	
	for con in tvcc:
	  print_con(t,(set(curcon) - set(con)),'down')
	  print_con(t,(set(con) - set(curcon)),'up')
	  t=t+1
	  curcon = con[:]
	  if t==21600: break

