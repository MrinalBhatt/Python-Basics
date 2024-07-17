#create generator objects
sqr = (i * i for i in range(1,10))

#iterate items from generator objects
for x in sqr:
    print(x)