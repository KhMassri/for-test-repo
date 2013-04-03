import random

def pullFrom(list):
    return random.choice(list)

def sim(k,G,alpha,beta):
    
    C1_K=[i for i in range(0,int(alpha*k+0.5))]
    C2_K=[i for i in range(int(alpha*k+0.5),k)]
    #print C1_K, C2_K
    
    sumc1=0.0
    sumc2=0.0
    sumc=0.0
    count=0.0
    for seed in range(1,10):        
        for trial in range(10000):
            count=count+1
            seenFromC1=[]
            seenFromC2=[] 
            c=0
            c1=0
            c2=0
            while len(seenFromC1+seenFromC2) < G:
                c=c+1
                if random.random()<beta:
                    if len(C1_K)>0:
                        pkt = str(pullFrom(C1_K))
                        if pkt not in seenFromC1:
                            seenFromC1.append(pkt)
                            c1=c1+1
                elif len(C2_K)>0:
                    pkt = str(pullFrom(C2_K))
                    if pkt not in seenFromC2:
                        seenFromC2.append(pkt)
                        c2=c2+1
            sumc1+=c1
            sumc2+=c2
            sumc+=c
        random.seed(random.random()*seed**seed)
        
    return sumc/count
    
