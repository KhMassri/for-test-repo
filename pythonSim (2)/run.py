import analysis
import simulation


G=20
K= 40
Beta = [0.25,0.5,0.75]
Alpha = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

            
anaRes=[]
simRes=[]

for beta in Beta:
    anaRes.append([analysis.ana(K,G,alpha,beta) for alpha in Alpha])
    simRes.append([int(simulation.sim(K,G,alpha,beta)) for alpha in Alpha])
        
print 'K2Galpha = ',Alpha,';'
print 'K2Gbeta = ',Beta,';'
print 'K2GanaRes = [',
for lst in anaRes:
  print lst,';'
print '];'
        
print 'K2GsimRes = [',
for lst in simRes:
  print lst,';'
print '];'
  

'''
anaRes = [analysis.ana(k,G,Alpha,Beta) for k in K]
simRes = [int(simulation.sim(k,G,Alpha,Beta)) for k in K]
        
print 'KG30 = ',K,';'
print 'anaResKG30 = ',anaRes,';'
print 'simResKG30 = ',simRes,';'


for beta in Beta:
    anaRes.append([analysis.ana(K,G,alpha,beta) for alpha in Alpha])
    simRes.append([ int(simulation.sim(K,G,alpha,beta)) for alpha in Alpha])
        
print 'alpha = ',Alpha,';'
print 'beta = ',Beta,';'
print 'anaRes = [',
for lst in anaRes:
  print lst,';'
print '];'
        
print 'simRes = [',
for lst in simRes:
  print lst,';'
print '];'
'''
