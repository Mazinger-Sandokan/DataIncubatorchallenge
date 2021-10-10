
### This is the script for Section 3 of the Data Incubator challenge. The question is about
# Buildings and Lasers. I wrote three possible solutions.

#SOLUTION 1 Brute force calculation of the np.mean and standard deviation. This works for the 
# first two questions and maybe even for questions 3 and 4. However, it fails when there are 20
#buildings
# SOLUTION 2 A solution that uses basic combinatorics to reduce a sum with ~N-factorial terms to a sum
# with ~N^3 terms. The idea is simple: Instead of computing the sum over all permutations of the
# sum of the distance travelled from each building, one interchanges the order of the sumation.
# It turns out that the total distance travelled for a Laser shot from each building over all
# permutations can be computed as a sum with ~N^2 terms which are simple combinatorial numbers.
### One CAVEAT is that, for simplicity, the second solution does not allow to specify
## arbitrary heights of the buildings. This was done because the instances asked did not required that.
## It could be modified easily to cover more cases in case it was needed.
# SOLUTION 3. In order to double check the second solution one can do a version of the brute force solution
# where instead of computing the average for all possibilities one chooses a random sample. One sees
### that for sufficiently large sample sizes the two solutions converge.






# import pandas
# import matplotlib
# from manimlib.utils.iterables import resize_array
import random
import itertools
# import statistics
# from statistics import np.mean
# from statistics import stdev
# from statistics import np.stddev
import math
import numpy as np


##This list contains the heights of the buildings.

heights=list(range(11))

### For instance, in the first questions, the heights are 1,1,3,4. There are 5 possible locations besides
#the 0th which is left free. For this reason we add one height=0 in hte list, to account
## for the one empty place in positions 1,2,3,4,5.

# N is the number of buildings
N=len(heights)-1
print("The number of buildings is "+ str(N))
#### SOLUTION 1: THE NAIVE COMPUTATION

### The set of posibilities is the set of all possible permutations of the list heights.
### We create a list called "posibilities"that contains all the permutations.


##Since there first slot is always empty, we add that information to the list
# of possible arrangements.
# posibilities=list(map(lambda z: list(z),itertools.permutations(heights)))
# posibilities=list(map(lambda z: [0]+z,posibilities))
# print(posibilities)
# print(len(posibilities))



### We create a function V='sum of distances from all buildings' which computes the values of V for a given arrangement:
def V(buildings):
    length = 0
    for i in range(1,len(buildings)):
        if buildings[i]>0: #### There are no buildings of height 0, and no laser is shot from the empty spot
            for j in range(1,i+1):
                length=length+1
                if buildings[i-j]>=buildings[i]:
                    break        
    return length




# Values=list(map(lambda z: V(z), posibilities))

### We now compute the np.mean of the values over all possibilities
# print(V([1,3,4,1,0]))
# print(' According to brute force, the np.mean is '+'{0:.10f}'.format(np.mean(Values)))
# print('According to brute force, the standard deviation is '+'{0:.10f}'.format(np.std(Values)))

####Solution 2 COMBINATORICS. We observe that the sum of V over all permutations
## can be computed as a sum of V_i the total distance travelled by shots from building i.
### this in turn is a sum over j,k of k W_{ijk} where W_{ijk} is the number of configurations
## where the i-th building is in the j-th positioSo The whole sum n and the ray travels distance k.
## The numbers W_{ijk} are given by combinatorial expressions. 
##


def W(i,j,k,n):
    res=0
    if i-k+1>=0 and i>0:
        if j==k:
            res=math.factorial(i)*math.factorial(n-k+1)/math.factorial(i-k+1)
        elif 1<=k and k<j:
            res=math.factorial(i)*math.factorial(n-k)*(n-i)/math.factorial(i-k+1)
    return res


# ans=0
# for i in range(1,N+1):
#     for j in range(1,N+2):
#         for k in range(1,N+2):
#             ans=ans+k*W(i,j,k,N)

##### We print the average of V which is the total sum of distances travelled divided by
### The number of possibilities, which is (N+1) factorial

# print('According to combinatoriacs, the np.mean is '+'{0:.10f}'.format(ans/math.factorial(N+1)))   

# exit()

####  Solution 3: Random Sampling. In order to double check we do some random sampling 
### and compute that averages on the samples.

Sample=[]
for i in range(3000000):
    Sample.append([0]+list(np.random.permutation(heights)))
SValues=list(map(lambda z:V(z),Sample))    
print('Statistically, the np.mean is '+'{0:.10f}'.format(np.mean(SValues)))
print('Statistically, the standard deviation is  '+'{0:.10f}'.format(np.std(SValues)))
# vari=0
# for v in Values:
#     vari=vari+(v-np.mean(Values))**2
# vari=vari/120
# SValues=list(map(lambda z:V(z),Sample))
# # print('{0:.10f}'.format(math.sqrt(vari)))
# # print('{0:.10f}'.format(np.stddev(Values)))
# print('{0:.10f}'.format(np.mean(SValues)))
# print('{0:.10f}'.format(stdev(SValues)))
# print(max(SValues))



# print(max(Values))

# def W(i,j,k,n):
#     res=0
#     if i-k+1>=0 and i>0:
#         if j==k:
#             res=math.factorial(i)*math.factorial(n-k+1)/math.factorial(i-k+1)
#         elif 1<=k and k<j:
#             res=math.factorial(i)*math.factorial(n-k)*(n-i)/math.factorial(i-k+1)
#     return res
# # print(W(3,1,1,5))

# ans=0
# for i in range(1,N+1):
#     for j in range(1,N+2):
#         for k in range(1,N+2):
#             ans=ans+k*W(i,j,k,N)
# print(ans)           






# # listagrande = []
# # d = {}
# # for fila in f:
# #     lista = file.split(',')
# #     listagrande.sppend(lista)
# #     d[lista[0]] = lista[1:]


