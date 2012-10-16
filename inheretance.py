class person:
   def __init__ (self,name,lunch):
      self.name = name
      self.lunch = lunch
   def getname(self):
      return self.name

class man(person):
   def getlunch(self):
      return self.lunch

class woman(person):
   def __init__ (self,name,lunch,prefer):
      self.name = name
      self.lunch = lunch
      self.prefer = prefer
   def getlunch(self):
      return self.lunch + " but would prefer "+ self.prefer
   def __str__ (self):
      return "A great beauty called "+self.name

course = [man("Daniel","Cod and peas"),man("David","Steak Pie"),man("Graham","Plaice")]

evening = course[:]
evening.append(woman("Lisa","Virtual Curried Mushrooms","Grape Juice"))

course[1].lunch = "Rock Salmon"

print "LUNCH"
for chap in course:
   print chap.getname()+": "+chap.getlunch()

print "and EVENING"
for chap in evening:
   print chap.getname()+": "+chap.getlunch()
   print chap
