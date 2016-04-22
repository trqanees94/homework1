def selectionsort (a):
	for i in range(len(a)):
		least = i
		for k in range(i+1, len(a) ):
			if a[k] < a[least]:
				least = k
		swap(a,least,i)
def swap(A,x,y):
	tmp=A[x]
	A[x]=A[y]
	A[y]=tmp


def insertionsort(b):
	for i in range(1, len(b)):
		value=b[i]
		position=i
		while position>0 and b[position-1]>value:
			b[position]=b[position-1]
			position=position-1
		b[position]=value



def mergesort( c):
  _mergesort( c, 0, len( c ) - 1 )
 
 
def _mergesort( c, first, last ):
  
  mid = ( first + last ) / 2
  if first < last:
    _mergesort( c, first, mid )
    _mergesort( c, mid + 1, last )
 
  
  a, f, l = 0, first, mid + 1
  tmp = [None] * ( last - first + 1 )
 
  while f <= mid and l <= last:
    if c[f] < c[l] :
      tmp[a] = c[f]
      f += 1
    else:
      tmp[a] = c[l]
      l += 1
    a += 1
 
  if f <= mid :
    tmp[a:] = c[f:mid + 1]
 
  if l <= last:
    tmp[a:] = c[l:last + 1]
 
  a = 0
  while first <= last:
    c[first] = tmp[a]
    first += 1
    a += 1
	

import matplotlib.pyplot as plt
import numpy as np
import timeit

MS=[]
MSR=[]
IS=[]
ISR=[]
SS=[]
SSR=[]

b=np.random.randint(9, size=10)
print(b)
insertionsort(b)
print(b)

#t1=timeit.Timer(lambda:insertionsort(b))

for x in range(1,10):
	a=np.random.randint(9, size=100*x)  #creates random array length 10 with integers from 0-4
	

	mergesort(a)	#insertionsort orders array b
		
	reverseA=a[::-1]

	t1=timeit.Timer(lambda:selectionsort(a))
	t2=timeit.Timer(lambda:selectionsort(reverseA))

	#t2=timeit.Timer(lambda:insertionsort(reverseB))

	#t1=timeit.Timer(lambda:mergesort(a))
	#t2=timeit.Timer(lambda:mergesort(reverseA))



	MS.append((t1.timeit(number = 1)))
	MSR.append((t2.timeit(number = 1)))

print(MS)
print(MSR)

#IS.append((x1.timeit(number=1)))
#ISR.append((x2.timeit(number=1)))

#SS.append((z1.timeit(number=1)))
#SS.append((z2.timeit(number=1)))

#plt.figure(1)
lines = plt.plot(MS)
plt.setp(lines, color='g')

lines2 = plt.plot(MSR)
plt.setp(lines2, color='r')

plt.ylabel('time in seconds * 10^-3')
plt.xlabel('number n elements in list')



plt.plot(MS)
plt.plot(MSR)
plt.show()


