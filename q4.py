import matplotlib.pyplot as plt
import numpy as np
import timeit

MS=[]

IS=[]

SS=[]

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



def insertionsort(b):
	for i in range(1, len(b)):
		value=b[i]
		position=i
		while position>0 and b[position-1]>value:
			b[position]=b[position-1]
			position=position-1
		b[position]=value

sumM=0.0
sumS=0.0
sumZ=0.0
for x in range(1,10):
	a=np.random.randint(9, size=100*x) 

	
	for x in range(1,101):
		arr=np.random.permutation(a)
		m1=timeit.Timer(lambda:mergesort(arr))
		sumM+=m1.timeit(number=1)

		arr=np.random.permutation(a)
		s1=timeit.Timer(lambda:selectionsort(arr))
		sumS+=s1.timeit(number=1)

		arr=np.random.permutation(a)
		z1=timeit.Timer(lambda:insertionsort(arr))
		sumZ+=z1.timeit(number=1)

	MS.append(sumM/100)
	SS.append(sumS/100)
	IS.append(sumZ/100)	
lines = plt.plot(MS)
plt.setp(lines, color='g')

lines2 = plt.plot(SS)
plt.setp(lines2, color='r')

lines3 = plt.plot(IS)
plt.setp(lines3, color='b')


plt.ylabel('time in seconds ')
plt.xlabel('number n elements in list')

plt.plot(MS)
plt.plot(IS)
plt.plot(SS)

plt.show()		