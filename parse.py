logfile = open("logfile.txt", "r").readlines()
KEYWORDS = ['test', 'text']
counterline = []
counter = 0
for line in logfile:
    for word in line.split():
        counter+=1
        if word in KEYWORDS:
            counterline.append(counter)
            print word
print KEYWORDS
print counterline
