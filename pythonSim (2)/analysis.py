import math
import random



def ana(K,G,alpha,beta):
    ''' analysis framework'''
    historyB=[]
    historyB_1=[]
    def incB(i):
        if alpha==0 or beta ==0:
            return 0
        if i==0 or i==1:
            return beta*i
        if i<len(historyB):
            return beta*(1-(1/(alpha*K))*(sum(historyB[0:i])))
            
        return beta*(1-(1/(alpha*K))*(sum([incB(j) for j in range(1,i)])))
        
    
    def incB_1(i):
        if alpha==1 or beta ==1:
            return 0
        if i==0 or i==1:
            return (1-beta)*i
        if i<len(historyB_1):
                return (1-beta)*(1-(1/((1-alpha)*K))*(sum(historyB_1[0:i])))
        
        return (1-beta)*(1-(1/((1-alpha)*K))*(sum([incB_1(j) for j in range(1,i)])))

    iter=0
    while (sum(historyB)+sum(historyB_1)) < G:
        historyB.append(incB(iter))
        historyB_1.append(incB_1(iter))
        iter=iter+1
    
    return iter
    
    
    

    


    #for i in range(1,iter):
     #   print i,historyB[i],historyB_1[i]
    #print "========================================================"
    #print "classe1 sum = ",sum(historyB)," From its content = ",alpha*K
    #print "classe2 sum = ",sum(historyB_1)," From its content = ",(1-alpha)*K
    #print "========================================================"
    #print "Total = ",(sum(historyB)+sum(historyB_1))
    #print "Ratio = ",sum(historyB)/(sum(historyB)+sum(historyB_1)),sum(historyB_1)/(sum(historyB)+sum(historyB_1))

