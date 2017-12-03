import random
import math

SIZE = 2**10
data = range(SIZE)
#low = 0
#high = SIZE - 1
#i = (high + low)/2
target = random.randrange(SIZE)

#print("-" * 80)
#print(SIZE)
#print(target)
#print("-" * 80)

def findMe(searchVal, dataSource):
    low = 0
    high = len(dataSource) - 1
    i = (high + low) / 2
    count = 0
    while searchVal != dataSource[i] and high != low:
        #print ('{%s --> %s[%s] <-- %s}' % (low, searchVal, i, high))
        if searchVal < data[i]:
            high = i - 1
        else:
            low = i + 1
        i = (high + low) / 2
        count += 1
    else:
        #print("found at %s in %s tries" % (i, count))
        return count

#print("======================== %s ========================" % "RANDOM")
#findMe(target, data)
#print("======================== %s ========================" % "FIRST")
#findMe(0, data)
#print("======================== %s ========================" % "LAST")
#findMe(SIZE - 1, data)

print ("log2(%s) = %d" %(SIZE, math.log(SIZE, 2)))
l = [(x, findMe(x, data)) for x in data]
