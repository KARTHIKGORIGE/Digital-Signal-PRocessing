#appending one array into another array
import numpy as np
a=input('enter the array')
b=input('enter the second array')
#using for loop
for i in range(0,len(b)):
	c=a.append(b[i])

print c
#using numpy code
d=np.append(a,b)
print d


